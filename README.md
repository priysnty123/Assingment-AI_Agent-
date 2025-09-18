**AI Agent Chatbot**


**🚀 Idea Behind the Application**

The idea is to build an AI-powered conversational assistant that can:

1. Answer user queries using an LLM.

2. Search the internet for up-to-date information.

3. Visit and extract content from specific websites.
   
4. Perform calculations when needed.



**⚙️ How It Works (Architecture / Approach)**


**1.**Frontend (Streamlit App)****

   Provides a chat interface where users can ask questions.
 
   Maintains chat history using st.session_state.
 
   Includes a Delete Chat button to reset the session and start a fresh conversation.
   

**2.**Backend (Agent System)****

   Uses LangGraph’s ReAct agent to orchestrate reasoning + tool usage.

   Every conversation is tied to a unique thread_id (session ID), ensuring context-aware
   responses.

   The agent can decide when to call external tools (search, website visit, calculator).
   

**3.**Tools Integrated****

   DuckDuckGo Search - Retrieves live internet results.
 
   Website Visitor - Fetches and converts webpage content into Markdown for better  eadability.
 
   Calculator - Evaluates mathematical expressions.


**4.**Memory Handling****

   Implemented using MemorySaver from LangGraph.
 
   Ensures continuity of conversations across multiple queries in the same session.
   

5.**Deployment**

   Built with Streamlit, making it easy to run locally or deployed free on Streamlit   Itself.



**🛠️ Tools & Frameworks Used**

  LangGraph - For building the ReAct-style agent with memory.

  LangChain Community Tools - For integrating DuckDuckGo search.

  LangChain Groq - For connecting to Groq-hosted LLMs (qwen/qwen3-32b).

  Streamlit - For the frontend chat interface.

  Requests + Markdownify - To fetch and format website content.

  dotenv - For managing API keys and environment variables.


