from langchain_core.tools import tool
import re 
import requests
from markdownify import markdownify

@tool
def website_visit(url :  str ) -> str:
    """
        Visit and extract content from a specific webpage URL provided by the user (such as company websites, 
        e-commerce product pages, government portals, or university ranking sites). The content is converted 
        into clean markdown format for easier reading. 

        Only use this tool when the user explicitly provides a valid link (http/https) and wants details, 
        summaries, or insights from that exact page. Do not use this tool for general information requests 
        or when no URL is given — in those cases, use duckduckgo_search instead.  

        Always include the original link in the final answer so the user can verify the source.
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
    Search the internet in real time using DuckDuckGo to retrieve the latest information, including 
    general knowledge updates, news, product prices, election results, sports scores, stock market 
    data, weather, or anything else that may have changed recently. 

    Always use this tool for time-sensitive or factual queries where accuracy depends on up-to-date 
    information — never rely on memory for such questions.  

    Examples: 
    - "What is the latest iPhone price in India?"  
    - "Who won the recent state elections?"  
    - "Show me today’s cricket match score."  
    - "What’s the current weather in Delhi?"  

    If there is any doubt about whether freshness matters, always call this tool. 
    Return concise summaries with sources or snippets when possible.
"""


 )
)