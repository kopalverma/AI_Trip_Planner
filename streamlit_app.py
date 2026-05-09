import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="🌍 AI Trip Planner",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar
with st.sidebar:
    st.title("🌍 AI Trip Planner")
    st.markdown("---")
    st.markdown("### About")
    st.markdown("An agentic AI travel planner powered by LangGraph ReAct agent with 8+ API integrations.")
    st.markdown("### Tech Stack")
    st.markdown("- 🧠 LangGraph + Groq\n- ⚡ FastAPI\n- 🎨 Streamlit\n- 🗺️ Google Places\n- 🌤️ OpenWeatherMap\n- 💱 ExchangeRate API")
    st.markdown("---")
    st.markdown("Built by **Kopal Verma**")
    st.markdown("[GitHub](https://github.com/kopalverma24) | [LinkedIn](https://linkedin.com/in/kopalverma)")

# Custom theme
st.markdown("""
<style>
.stTextInput > div > div > input {
    border-radius: 10px;
}
.stButton > button {
    border-radius: 10px;
    background-color: #FF6B6B;
    color: white;
    font-weight: bold;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI Trip Planner")
st.caption("Ask me anything about your next trip!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("e.g. Plan a 5 day trip to Goa...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Planning your trip..."):
            try:
                response = requests.post(f"{BASE_URL}/query", json={"question": user_input})
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer returned.")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error("Backend failed to respond: " + response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")