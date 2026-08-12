from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.chat_models import ChatTongyi

@tool(description="获取体重，返回值是整数，单位千克")
def get_weight()->int:
  return 90

@tool((description="获取身高，返回值是整数，单位厘米")
def get_height()->int:
return 178

agent=creat_agent(
  model=ChatTongyi(model="qwen3-max"),
  tool=[get_weight,get_height],
  system_prompt="""你是一个严格遵循ReAct框架的智能体，必须按[思考-行动-观察-再思考]的流程来解决问题，
    且**每轮仅能思考并调用一个工具**，禁止单次调用多个工具。
    并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我""",
)

for chunk in agent.stream(
  {"messages":[{"role":"user","content":"计算我的BMI"}]},
  stream_mode=values
)

lastest_message=chunk["messages"][-1]

if lastest_message.content:
  print(type(lastest_message).__name__,lastest_message.content)

try:
  if lasteat_message.tool_calls:
    print(f"工具调用：[{tc['name'] for tc in lastest_message.tool_calls]}")

excepyt AttributeArror as e:
pass
