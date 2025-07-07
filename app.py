from dotenv import load_dotenv
import streamlit as st
import os 
import sqlite3 
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key for Google Gemini
API_KEY = os.getenv("GENAI_API_KEY")
genai.configure(api_key=API_KEY)

# Database and table configuration
DB_FILENAME = "employee.db"
TABLE_NAME = "EMPLOYEE"

# Load Google model and provide SQL query as a response
def get_gemini_response(question, prompt):
    if isinstance(prompt, list):
        prompt = ''.join(prompt)
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    response = model.generate_content(f"{prompt}\n{question}")
    generated_sql = response.text.strip()
    cleaned_sql = clean_sql_query(generated_sql)
    return cleaned_sql

# Function to clean SQL query (removes unwanted characters)
def clean_sql_query(sql):
    sql = sql.replace('`', '').strip()
    # Remove markdown code block if present
    if sql.startswith('sql'):
        sql = sql[3:].strip()
    sql = sql.replace('```', '').strip()
    return sql

# Retrieve query from SQL data
def read_sql(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        rows = f"SQL Error: {e}"
    finally:
        conn.close()
    return rows

# Function to clean the output result (remove brackets and quotes)
def clean_output(row):
    return ', '.join([str(item) for item in row])

# Updated prompt for EMPLOYEE database
prompt = f"""
You are an expert SQL assistant. Your task is to convert natural language questions into accurate SQL queries based on the following database schema.

The database is named `{DB_FILENAME}` and contains a table `{TABLE_NAME}` with these columns:
- ID (integer, primary key)
- NAME (string)
- DEPARTMENT (string)
- ROLE (string)
- EMAIL (string)
- SALARY (integer)
- DATE_JOINED (date)

For every question, generate a well-structured SQL query that:
1. Selects only the necessary columns.
2. Uses appropriate filtering (e.g., WHERE, LIKE, etc.) based on the question.
3. Avoids any unnecessary characters, including backticks, extra spaces, or markdown formatting.
4. Does not include any surrounding markdown, such as ```sql.

Examples:
1. Question: "How many employees are in the Engineering department?"
   SQL: SELECT COUNT(*) FROM EMPLOYEE WHERE DEPARTMENT='Engineering';

2. Question: "List the names and emails of employees who joined after 2020-01-01."
   SQL: SELECT NAME, EMAIL FROM EMPLOYEE WHERE DATE_JOINED > '2020-01-01';

3. Question: "What is the average salary in the HR department?"
   SQL: SELECT AVG(SALARY) FROM EMPLOYEE WHERE DEPARTMENT='HR';

Now, convert the following question into an SQL query:
"""

## Streamlit App

st.set_page_config(page_title="SQL Query Retrieval")
st.header("Gemini App To Retrieve SQL Data")

# Input question from the user
question = st.text_input("Input your question about the employee database:", key="input")

# Button to submit the question
submit = st.button("Ask the question")

if submit and question:
    response = get_gemini_response(question, prompt)
    st.code(response, language="sql")  # Show the generated SQL for transparency

    # Execute the SQL query and display the result
    result = read_sql(response, DB_FILENAME)
    st.subheader("The response is:")
    if isinstance(result, str):
        st.error(result)
    elif result:
        for row in result:
            cleaned_row = clean_output(row)
            st.write(cleaned_row)
    else:
        st.info("No results found.")
