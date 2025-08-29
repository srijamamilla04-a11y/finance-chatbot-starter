import streamlit as st
import requests
import json

st.set_page_config(page_title="Finance Chatbot", layout="wide")
st.title("💰 Personal Finance Chatbot (RAG + Budget Advisor)")

tab1, tab2 = st.tabs(["Ask (RAG)", "Budget Summary"])

with tab1:
    st.subheader("Ask grounded questions (uses PDF knowledge base)")
    q = st.text_input("Your question")
    k = st.slider("Top-k context chunks", 1, 8, 3)
    if st.button("Ask"):
        try:
            r = requests.post("http://127.0.0.1:8000/ask", json={"query": q, "k": k})
            data = r.json()
            if "error" in data:
                st.error(data["error"])
            else:
                st.markdown("### Answer")
                st.write(data["answer"])
                with st.expander("Context used"):
                    st.write(data["context"])
        except Exception as e:
            st.error(f"Request failed: {e}")

with tab2:
    st.subheader("Budget summary & recommendations")
    income = st.number_input("Monthly income", min_value=0.0, value=50000.0, step=1000.0)
    expenses_json = st.text_area("Expenses JSON", value='{"rent": 15000, "food": 8000, "transport": 3000, "utilities": 2500}')
    goal = st.text_input("Savings goal", "Emergency fund")
    persona = st.selectbox("Persona", ["student", "professional"])
    if st.button("Get Summary"):
        try:
            expenses = json.loads(expenses_json)
        except Exception as e:
            st.error(f"Invalid JSON: {e}")
            expenses = None
        if expenses is not None:
            payload = {"income": income, "expenses": expenses, "goal": goal, "persona": persona}
            try:
                r = requests.post("http://127.0.0.1:8000/budget-summary", json=payload)
                data = r.json()
                st.markdown("### Summary")
                st.write(data)
            except Exception as e:
                st.error(f"Request failed: {e}")
