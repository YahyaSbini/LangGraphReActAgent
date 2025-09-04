import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState,StateGraph, END

from nodes import run_agent_reasoning, tool_node
load_dotenv()

#Those are states
Agent_Reason = "agent_reason"
Act = "act"
Last = -1
#in python you can access last item by (-1)

def should_continue(state: MessagesState) -> str:
    if not state["messages"][Last].tool_calls:
        return END
    return Act
# if END: it means stop the work flow here

#MessagesState: this holds the state ,Human-Message ,Tool-message (Updated by Act) and AI-message (updated by Agent_reason)
flow = StateGraph(MessagesState) #creating the graph
flow.set_entry_point(Agent_Reason)
flow.add_node(Agent_Reason, run_agent_reasoning)
flow.add_node(Act, tool_node)

flow.add_edge(Act, Agent_Reason)
flow.add_conditional_edges(Agent_Reason,should_continue ,{
    END:END,
    Act:Act})
#after updating the state from agent_reason check if you should continue or not, if not so you are in the End Node ,else in the Act Node
app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="flow.png")


if __name__ == '__main__':
    print("Hello ReAct LangGraph with Function Calling")
    res = app.invoke({"messages": [HumanMessage(content="Hi,please tell me the temp in Damascus from only one resource then multiply it by 3.")]})
    print(res["messages"][Last].content)