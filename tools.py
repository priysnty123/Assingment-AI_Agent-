from langchain_core.tools import tool
import re 
import requests
from markdownify import markdownify

@tool
def website_visit(url :  str ) -> str:
    """
    Visit a specific webpage URL (such as company websites, e-commerce product pages, government portals, 
    or university ranking sites) to extract the main content in clean markdown format. 

    Use this tool only when the user explicitly provides a valid link and wants details or summaries 
    from that page, rather than general information or search results. 

    Always include the original link in your final response so the user can verify the source.

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
        """"
        Search the internet in real time using DuckDuckGo to retrieve the latest information, Answering the general knowledge question, news, 
        updates, product prices, election results, sports scores, stock market data, weather, or 
        anything else that may have changed recently. 

        Always use this tool for time-sensitive or factual queries where accuracy depends on up-to-date 
        information, instead of relying on memory.  

        Examples: 
        - "What is the latest iPhone price in India?"  
        - "Who won the recent state elections?"  
        - "Show me today’s cricket match score."  
        - "What’s the current weather in Delhi?"  

        Never attempt to answer these questions from memory — always call this tool. 
        Return concise summaries with sources or snippets when possible.
"""

 )
)