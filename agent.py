from dotenv import load_dotenv

load_dotenv()

import os



from  langchain_groq import  ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage
from ddgs import DDGS
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools import website_visit , calculator, search_tool

load_dotenv()

model = ChatGroq(model_name="qwen/qwen3-32b", temperature=0) #model="llama-3.3-70b-versatile"
memory = MemorySaver()


tools = [search_tool,website_visit,calculator]
model = create_react_agent(model,tools, checkpointer=memory )


# config = {"configurable": {
#         "thread_id": "1abc"
#     }}


def ask_agent(query:str, session_id: str  ):
       
 # Use the unique session_id for the thread
 config = {"configurable": {
        "thread_id": session_id 
      }}  
 
 response = model.invoke(
    {"messages": [HumanMessage(content=query)]},
    config=config
)


 for message in response["messages"]:
   print(f"========{message.type}==========")
   print(message.content, "\n")
   
   if hasattr(message, "tool_calls"):
      print(message.tool_calls, "\n")



 return response["messages"][-1].content