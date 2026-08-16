# 练习 04：Agent 中间件（Middleware）

## 功能说明
- 展示 LangChain Agent 的生命周期钩子函数
- 通过中间件在 Agent 执行的不同阶段插入自定义逻辑
- 实现 Agent 执行前后、模型调用前后、工具调用的监控

## 核心知识点
- **中间件装饰器**：`@before_agent`、`@after_agent`、`@before_model`、`@after_model`、`@wrap_model_call`、`@wrap_tool_call`
- **Agent 生命周期**：Agent 启动 → 模型调用 → 工具调用 → 模型调用 → Agent 结束
- **`AgentState`**：包含消息列表等状态信息
- **`Runtime`**：运行时的上下文对象

## 中间件执行顺序
[before_agent] Agent 启动前
[before_model] 模型调用前
[wrap_model_call] 模型调用中（钩子）
[after_model] 模型调用后
[wrap_tool_call] 工具调用中（钩子）
[after_agent] Agent 结束后

## 运行
```bash
python app.py
