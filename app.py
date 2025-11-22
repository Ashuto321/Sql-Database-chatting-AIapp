#streamlit app
from dotenv import load_dotenv
load_dotenv() # load all the enviroment variables


import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load google model and provide sql query as a response
def get_gemini_response(question,prompt):
       model=genai.GenerativeModel('gemini-2.0-flash-exp')
       response=model.generate_content([prompt[0],question])
       return response.text


## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
   You are an expert AI assistant specializing in converting natural language questions into SQL queries.  

The SQL database is named **STUDENT** and contains the following columns:  
- **NAME** (VARCHAR)  
- **CLASS** (VARCHAR)  
- **SECTION** (VARCHAR)  
- **MARKS** (INT)  

Follow these guidelines when generating SQL queries:  
1. Ensure the output contains only the SQL query—do not include explanations, formatting markers (like triple backticks), or the word "SQL".  
2. Use proper SQL syntax while maintaining accuracy and efficiency.  
3. If the query involves filtering, apply appropriate `WHERE` clauses.  
4. If an aggregation is required (e.g., counting records, averaging values), use functions like `COUNT()`, `AVG()`, etc.  

#### **Examples**  

- **Question**: "How many student records are present?"  
  - **SQL Query**: `SELECT COUNT(*) FROM STUDENT;`  

- **Question**: "List all students in the Data Science class."  
  - **SQL Query**: `SELECT * FROM STUDENT WHERE CLASS = "Data Science";`  

Now, generate an SQL query for the given question.  


    """
]

## Streamlit App

# Set page configuration with a title and icon  
st.set_page_config(page_title="SQL Query Generator | Edureka", page_icon="🤖")  

# Display the Edureka logo and header  
st.image("123.png", width=200)  
st.markdown("🤖 Edureka's Gemini App – Your AI-Powered SQL Assistant!")  
st.markdown("🚀 Ask any question, and I'll generate the SQL query for you!")  

# User input for the question  
question = st.text_input("📝Enter your query in plain English:", key="input")  

# Submit button with an engaging design  
submit = st.button("🎯Generate SQL Query")  


# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)
