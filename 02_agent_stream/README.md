# 练习 02： Agent的流式输出

## 功能说明
- Agent 拥有两个工具：`get_price`（获取股价）和 `get_info`（获取公司介绍）
- Agent 根据用户问题自主决策调用一个或多个工具
- 使用 `stream` 流式输出，实时观察工具调用过程

## 核心知识点
- **多工具 Agent**：Agent 可以从工具列表中选择合适的工具
- **`stream_mode="values"`**：流式输出模式，逐次获取完整状态
- **`tool_calls`**：消息对象中的工具调用信息
- **自主决策**：LLM 根据用户提问决定调用哪个工具

## 运行
```bash
python app.py
