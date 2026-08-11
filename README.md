# 🤖 LangChain Agent（智能体）学习笔记

> 从零开始学习 LangChain Agent（智能体）的完整历程 —— 让 LLM 自主决策、调用工具、完成任务。

本仓库采用 **Monorepo（单一仓库）** 结构，每个文件夹都是一个独立的小练习，互不干扰，方便随时回顾和复用。

---

## 📂 项目列表

| 编号 | 文件夹 | 说明 | 核心知识点 |
| :---: | :--- | :--- | :--- |
| 01 | [01_agent_basic](./01_agent_basic) | Agent 初体验 | `create_agent`, `@tool`, 工具调用 |
| 02 | [02_agent_stream](./02_agent_multi_tools) | 多工具 Agent | 多工具选择, stream流式输出, tool_calls追踪 |
| 03 | 待更新 | - | - |

---

## 📂 项目结构
langchain-agent-learning/
├── README.md # 项目总说明
├── .gitignore # Git 忽略文件
├── LICENSE # MIT 许可证
│
├── 01_agent_basic/ # ✅ 已创建
│ ├── app.py # Agent 初体验主程序
│ └── README.md # 练习01的说明文档
│
├── 02_agent_multi_tools/              # ✅ 已创建
│   ├── app.py
│   └── README.md
│
└── 03_xxx/                            # 📅 待创建

---

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/你的用户名/langchain-agent-learning.git
cd langchain-agent-learning
