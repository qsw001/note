# tool 

## tool 能干什么

tool是给大模型用的函数接口，模型只能“说话”，tool可以使模型调函数，查数据，做计算，执行你写好的逻辑。

## tool怎么写

tool的本质就是一个python函数，其最小的组成部分有：
- @tool: 将普通函数注册为tool
- (city: string): 必须有类型注释
- -> string: 告诉模型的返回类型
- docstring: 模型用来判断什么使用调用工具

