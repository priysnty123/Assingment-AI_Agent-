from langchain_core.tools import tool
import re 
import requests
from markdownify import markdownify

@tool
def website_visit(url :  str ) -> str:
    """
        Use this tool to visit URLs obtained from the search results or provided directly by the user, 
        and extract the main content of the webpage in clean markdown format. 
        Do not use this tool for general queries without a valid URL.
    
    Args:
        url (str): The URL of the webpage to visit.
    
"""

    
    #send request 
    response = requests.get(url , timeout = 20 )
    
    
    #check is request is succesful
    response.raise_for_status()
    
    
    # convert the HTML to markdown
    html_content = response.text
    markdown_content = markdownify(html_content).strip()
    
    markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
    
    # Return the processed markdown, trimming to a reasonable length
    return markdown_content[:5000] #trim to 5k chars max




#print(website_visit.invoke("https://www.apple.com"))


@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import Tool

search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="duckduckgo_search",
    func=search.run,
    description=(
    """
        Always use this tool to fetch the latest or up-to-date information, including news, 
        general knowledge updates, election results, product prices, sports scores, stock 
        market data, and weather. Never answer such queries from memory — always search 
        the internet in real time.

        Examples:
        - "What is the latest iPhone price in India?"
        - "Who won the 2025 Delhi elections?"
        - "Show me today’s cricket match score between India and Pakistan."
        - "What is the current weather in Mumbai?"
        - "Latest stock price of Reliance Industries today"
"""


 )
)