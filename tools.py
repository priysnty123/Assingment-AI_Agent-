from langchain_core.tools import tool
import re 
import requests
from markdownify import markdownify

@tool
def website_visit(url :  str ) -> str:
    """
    Visit a specific webpage URL (like any company websites,E-Commerece website, government websites, or university ranking pages) 
    to extract the main content in markdown format.
    Use this if the user wants details from a specific website rather than just a search result.
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
    description=("Use this tool for any query that requires up-to-date, real-time, General Knowledge Question or factual information "
                 "from the internet. Examples include: latest news, election results, product prices, stock "
                 "market updates, sports scores, weather, or anything that may have changed recently. "
                 "Do not attempt to answer these from memory — always call this tool instead."
 )
)