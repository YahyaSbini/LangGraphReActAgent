from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import OpenAI, ChatOpenAI
from langchain_tavily import tavily_search, TavilySearch

load_dotenv()

@tool
def triple(num:float) -> float:
    """
    :param num: a number to be tripled
    :return: the triple of the input number
    """
    return float(num)*3

tools = [TavilySearch(max_results=1),triple]

llm = ChatOpenAI(model="gpt-5",temperature=0).bind_tools(tools)