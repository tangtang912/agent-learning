"""
Agent 练习 01：Agent 初体验
功能：创建一个简单的 Agent，可以调用天气查询工具
核心知识点：create_agent, @tool 装饰器, 工具调用
"""

from langchain_agents import create_agent
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool

@tool(describtion = "查询天气")
def get_weather()->str:
  return "晴天"

agent = create_agent(
  model = ChatTongyi(model = "qwen3-max"),
  tools = [get_weather],
  system_prompt = "你是一个聊天助手，可以回答用户问题"
)

res = agent.invoke(
  {
    "messages":[
      {"role":"user","content":"明天上海的天气如何？"},
    ]
  }
)

for msg in ["messages"]:
  print(type(msg)__name__,msg.content)
