"""核对交换资料的客户编号、时序和关联条件。"""
import json
from pathlib import Path
import unittest


SAMPLES = Path(__file__).resolve().parents[1] / "samples"


def rows(name):
    content = (SAMPLES / f"{name}.ndjson").read_text(encoding="utf-8")
    return [json.loads(line) for line in content.splitlines()]


class ExchangeSampleTest(unittest.TestCase):
    def test_records_are_json_objects(self):
        files = sorted(SAMPLES.glob("*.ndjson"))
        self.assertEqual(len(files), 4)
        for path in files:
            with self.subTest(path=path.name):
                records = rows(path.stem)
                self.assertTrue(records)
                self.assertTrue(all(isinstance(row, dict) for row in records))

    def test_related_records_preserve_source_evidence(self):
        assignment = {row["appointment"]: row for row in rows("appointments")}
        reads, handoff, other = rows("terminal")
        self.assertEqual(reads["rider"], handoff["rider"])
        self.assertEqual(handoff["pass"], assignment[handoff["appointment"]]["pass"])
        self.assertEqual(handoff["event"], other["event"])
        self.assertNotEqual(handoff["device"], other["device"])
        change = assignment["point-1"]["from"]
        self.assertLess(handoff["earliest"], change)
        self.assertGreater(handoff["latest"], change)
