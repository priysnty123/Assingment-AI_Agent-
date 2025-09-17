# import streamlit as st
# from agent import ask_agent

# st.title("AI Agent")
# with st.sidebar:
#    st.header ("")
   
   
# if query:= st.chat_input("Ask Me Anything!"):
#     st.chat_message("user").write(query)
#     response = ask_agent(query)
#     st.chat_message("assistant").write(response)

import streamlit as st
from agent import ask_agent
from streamlit.runtime.scriptrunner import get_script_run_ctx
import uuid  # Import this to generate new thread IDs

st.title("AI Agent")

# Initialize chat history (for the UI)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the agent's thread_id (for the backend memory)
if "thread_id" not in st.session_state:
    try:
        # Use the Streamlit session ID as the *first* thread_id
        session_id = get_script_run_ctx().session_id
    except Exception:
        session_id = "local_test_thread" # Fallback
    st.session_state.thread_id = session_id


# --- 2. Main Chat Interface ---

# Display all past messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- 3. NEW DELETE BUTTON LOCATION ---
# We create two columns. The first one (80%) is empty space.
# The second one (20%) holds our button. This pushes it to the right.
col_empty, col_button = st.columns([0.8, 0.2]) # 80% empty, 20% for button

with col_button:
    if st.button("Delete Chat"):
        # Clear the chat history from the UI
        st.session_state.messages = []
        
        # Generate a new, random thread_id to start a new conversation
        st.session_state.thread_id = f"thread_{uuid.uuid4()}"
        
        # Rerun the app to clear the chat from the screen
        st.rerun()

# --- 4. Handle new input ---
# st.chat_input will always appear at the very bottom,
# just under your new "Delete Chat" button.
if query := st.chat_input("Ask Me Anything!"):
    # Add user message to UI history
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    # Get response from the agent, using the *managed* thread_id
    response = ask_agent(query, st.session_state.thread_id) 

    # Add assistant message to UI history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)