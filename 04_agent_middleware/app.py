from langchain.agent import create_agent,AgentState
from langchain.agent.middleware import befor_agent,after_agent,before_model,after_model,wrap_model_call,wrap_tool_call
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool
from langgraph.runtime import Runtime

@tool（describtion="查询天气，传入天气名称，返回天气信息字符串）
def get_weather(city:str)->str:
  return f"{city}天气：晴天“


"""
1.agent执行前
2.agent执行后
3.model执行前
4.model执行后
5.工具执行中
6.模型执行中
"""

@before_agent
def log_before_agent(state:AgentState,runtime:RunTime)->None:
  print(f"[before_agent]agent启动，并附带{len(state[message'])} 消息" )

@before_model
def log_bofore_model(state_AgentState,runtime:Runtime)->None:
  print(f"[before_model]模型即将调用，并附带{len(state['message'])}消息")
  
@after_agent
def log_after_agent(state_AgentState,runtime:Runtime)->None:
  print(f"[after_agent]agent结束，并附带{len(state['messages'])}消息")

@after_model
def log_after_model(state:AgentState,runtime:Runtime)->None:
    print(f"[after_model]模型调用结束，并附带{len(state['messages'])}消息")

@wrap_model_call
def wrap_model_call(request,handle)->:
  print("模型调用啦")
  
@wrap_tool_call
def monitor_tool(request,handle):
  print(f"工具执行：{request_tool_call['name']}")
  print(f"工具执行传入参数：{request_tool_call['args']}")

  return hangdle(request)

agent=create_agent(
  model = ChatTongyi(model = "qwen3-max"),
  tools = [get_weather]
  middleware = [log_before_agent,log_after_agent,log_before_model,log_after_model,wrap_tool_call,wrap_model_call]

  res = agent.invoke(
    {"messages":[{"role":"user","content":"今天上海天气如何，如何穿衣"}]}
    )
  print(res["messages"][-1].content)

