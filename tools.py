from langchain_core.tools import tool
import re 
import requests
from markdownify import markdownify

@tool
def website_visit(url :  str ) -> str:
    """
        Use this tool to visit URLs obtained from the search results and extract the main content of the webpages in markdown format.
    Arg: 
        url: The url link of the webpage to visit
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
    Srtictly use this tool to Search the internet in real time using DuckDuckGo or ddgs tool to retrieve the latest information, including 
    (general knowledge updates, news, product prices, election results, sports scores, stock market 
    data, weather, or anything else that may have changed recently). 

    Always use this tool for time-sensitive or factual queries where accuracy depends on up-to-date 
    information — never rely on memory for such questions.  


    If there is any doubt about whether freshness matters, always call this tool. 
    Return concise summaries with sources or snippets when possible.
"""


 )
)