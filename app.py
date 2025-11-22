#streamlit app
from dotenv import load_dotenv
load_dotenv()  # load all environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure API Key (SDK only)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google model and provide SQL query as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")  # SDK-only model

    # Combine prompt and the user's question as one string (SDK recommended way)
    final_prompt = prompt + "\n\nUser Question: " + question

    response = model.generate_content(final_prompt)
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Your Prompt (SDK-only → must be a string not a list)
prompt = """
You are an expert AI assistant specializing in converting natural language
questions into SQL queries.

The SQL database is named STUDENT and contains these columns:
- NAME
- CLASS
- SECTION
- MARKS

Rules:
1. Only output the SQL query, nothing else.
2. No markdown or backticks.
3. Use correct SQL syntax.
4. Use WHERE, COUNT, AVG, etc. when needed.

Examples:
- Question: How many student records exist?
  Answer: SELECT COUNT(*) FROM STUDENT;

- Question: Show students in Data Science class.
  Answer: SELECT * FROM STUDENT WHERE CLASS = "Data Science";
"""

# Streamlit App
st.set_page_config(page_title="SQL Query Generator | Edureka", page_icon="🤖")
st.image("123.png", width=200)
st.markdown("🤖 **Edureka's Gemini App – Your AI-Powered SQL Assistant!**")
st.markdown("🚀 Ask any question, and I'll generate the SQL query for you!")

question = st.text_input("📝Enter your query in plain English:", key="input")

submit = st.button("🎯Generate SQL Query")

if submit:
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(sql_query)

    # Execute query
    try:
        result = read_sql_query(sql_query, "student.db")
        st.subheader("Query Result:")
        st.write(result)
    except Exception as e:
        st.error(f"SQL Error: {e}")
