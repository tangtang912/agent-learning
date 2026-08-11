# 练习 01：Agent 初体验

## 功能说明
- 使用 LangChain 的 `create_agent` 创建第一个智能体
- 定义一个简单的天气查询工具（`@tool` 装饰器）
- Agent 自主决定是否调用工具来回答用户问题

## 核心知识点
- **`create_agent`**：LangChain 官方 Agent 创建函数
- **`@tool` 装饰器**：将普通函数转换为 Agent 可调用的工具
- **Agent 执行流程**：用户输入 → Agent 决策 → 调用工具（可选）→ 生成回答

## 运行
```bash
python app.py
