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
        Always Striclty  use ddgs ot this  tool to fetch the latest or up-to-date information, including news, 
        general knowledge updates, election results, product prices, sports scores, stock 
        market data, and weather. Never answer such queries from memory. 

        Never rely on memory or mix memory with results. The final answer must always be 
        based solely on the search output.
        
        If the question contains words like 'current', 'latest', 'today', 'yesterday', or a specific year 
        (e.g., 2025), always call this tool — even if you think you already know the answer. 

Examples:
- "Who is the current CM of Delhi?"
- "What is the latest iPhone price in India?"
- "Show me today’s cricket match score."
- "Current stock price of TCS"
- "What’s the weather in Mumbai right now?"
"""


 )
)