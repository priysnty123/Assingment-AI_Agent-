## **AI Agent Chatbot**


## **🚀 Idea Behind the Application**

The idea is to build an AI-powered conversational assistant that can:

1. Answer user queries using an LLM.

2. Search the internet for up-to-date information.

3. Visit and extract content from specific websites.
   
4. Perform calculations when needed.



## **⚙️ How It Works (Architecture / Approach)**


## **1.**Frontend (Streamlit App)****

   1. Provides a chat interface where users can ask questions.
 
   2. Maintains chat history using st.session_state.
 
   3. Includes a Delete Chat button to reset the session and start a fresh conversation.
   

## **2.**Backend (Agent System)****

   1. Uses LangGraph’s ReAct agent to orchestrate reasoning + tool usage.

   2. Every conversation is tied to a unique thread_id (session ID), ensuring context-aware
   responses.

   3. The agent can decide when to call external tools (search, website visit, calculator).
   

## **3.**Tools Integrated****

   1. DuckDuckGo Search - Retrieves live internet results.
 
  2. Website Visitor - Fetches and converts webpage content into Markdown for better  eadability.
 
  3.  Calculator - Evaluates mathematical expressions.


## **4.**Memory Handling****

   1. Implemented using MemorySaver from LangGraph.
 
   2. Ensures continuity of conversations across multiple queries in the same session.
   

## 5.**Deployment**

  1. Built with Streamlit, making it easy to run locally or deployed free on Streamlit   Itself.



## **🛠️ Tools & Frameworks Used**

  1. LangGraph - For building the ReAct-style agent with memory.

  2. LangChain Community Tools - For integrating DuckDuckGo search.

  3. LangChain Groq - For connecting to Groq-hosted LLMs (qwen/qwen3-32b).

  4. Streamlit - For the frontend chat interface.

  5. Requests + Markdownify - To fetch and format website content.

  6. dotenv - For managing API keys and environment variables.


## 🏃‍♂️ How to Run the Project  

## 1. Clone the Repository  
```bash
git clone https://github.com/your-username/ai-agent-chatbot.git
cd ai-agent-chatbot
```

## 2. Create the Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Set Environment Variables

Create a .env file in the project root and add your API keys. Example:
```bash 
GROQ_API_KEY=your_groq_api_key_here
```

## 5. Run the Streamlit App
```bash 
Streamlit run app.py
```



