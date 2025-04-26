from dotenv import load_dotenv
load_dotenv()  # Load environment variables (if needed)

import streamlit as st
import os
import sqlite3
import requests  # For Hugging Face API calls

# Hugging Face Inference API (Free)
API_URL = "https://api-inference.huggingface.co/models/MBZUAI/LaMini-Flan-T5-248M"
HF_API_KEY = os.getenv("HF_API_KEY")  # Get your free API key from Hugging Face

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query_hf_model(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        st.error(f"Error calling Hugging Face API: {e}")
        return None

def get_sql_response(question, prompt):
    full_prompt = f"{prompt}\nQuestion: {question}\nSQL Query:"
    output = query_hf_model({"inputs": full_prompt})
    if output and isinstance(output, list):
        return output[0].get("generated_text", "").strip()
    return None

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return []

# Define prompt (simplified since the model is smaller)
prompt = """
Convert English questions to SQL queries for a STUDENT table with columns: NAME, CLASS, SECTION.
Example:
- Question: "List all students in Data Science class?"
- SQL: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
Do not include ``` or 'sql' in the output.
"""

# Streamlit UI
st.set_page_config(page_title="SQL Query Generator (Free Model)")
st.header("Ask a question about STUDENT database")

question = st.text_input("Enter your question:", key="input")
submit = st.button("Generate SQL & Run")

if submit and question:
    st.write("Generating SQL...")
    sql_query = get_sql_response(question, prompt)
    
    if sql_query:
        st.subheader("Generated SQL Query")
        st.code(sql_query, language="sql")
        
        st.subheader("Query Results")
        results = read_sql_query(sql_query, "student.db")
        if results:
            for row in results:
                st.write(row)
        else:
            st.warning("No results found.")
    else:
        st.error("Failed to generate SQL query.")