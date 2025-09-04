from dotenv import load_dotenv
from langgraph.graph import MessagesState, StateGraph,END
from langgraph.prebuilt import ToolNode #This is going to execute the funtions
from reAct import llm,tools
load_dotenv()

"""
selected functions are going to be executed here
"""
root_prompt = """You are a helpful assistant that can use tools to answer questions"""
#Messagestate : Dictionary has the key of messages (Human-AI chat)
def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning Node
    """
    response = llm.invoke([{"role":"system","content":root_prompt},*state["messages"]])
    # * : for unpacking
    return {"messages":[response]}

tool_node = ToolNode(tools)