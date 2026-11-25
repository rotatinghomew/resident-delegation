# 配送终端交接协议

`households` 仅含虚构联系代号。各 scope 是 create、arrange、view 中之一。授权 `mandates` 的 order 为 null 时适用指定住户的订单，非空时只适用该单。起止有效区间 [from, until)，撤销从 revoked_at 生效。住户和自己的付款人分别向接口提交请求。

`appointments` 区分最初和后来经确认的上门安排。detail 保存配送必需的地点和门禁代号；普通排班只含 appointment、时间段和指派骑手。骑手从到岗至转班只可按当前安排读取详情，历史披露可查询披露人、对象和时刻。payment 由自己付款的人持有。

`terminal` 中端侧记录用 (device, event) 识别。凭证 `pass` 绑定当次预约与持包骑手，回执携带实际交付证据编号 proof。终端时钟带误差范围，最早 earliest 与最晚 latest 都是可能发生之时。与撤销或改约的生效时刻交叠而证据不足时需人工处理。已交付的业务回执与此前发出的详情记录不应被覆盖。所有实体和凭证都是本地合成代号。

交换样本为 UTF-8 NDJSON，每行独立。文件中的行顺序保留这组资料的原始提供顺序。
