from dotenv import load_dotenv
load_dotenv() #Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai 

# Configure GenAI key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Create a function to load Google_Gemini model and
#This function is also responsible for giving the query as response
def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql_query, db_name):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    cur.execute(sql_query)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Defining the prompt
prompt=[
    """
    You are an exper in converting English text to SQL query!
    The SQL database has the name TEST and has the following columns- NAME, CLASS, 
    SECTION  \n\nFor example, \nExample 1 - How many entries of records are present ?,
    the SQL command will be something like this SELECT COUNT(*) AS COUNT FROM STUDENT;
    \nExample 2 - List out the students those who have taken DataScience class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS='DataScience' order by SECTION;
    also the SQL code should not have ''' in the beginning or end and SQL word in output  
    
    """
]

# Set-up the streamlit app
st.set_page_config(page_title="I can retrieve any SQL query", layout="wide")
st.header("Gemini app to retrieve SQL Data")


question=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

#If the submit is clicked, 
if submit:
    response=get_gemini_response(question,prompt)
    final_response=read_sql_query(response,"test.db")
    st.subheader("The response is: ")
    for row in final_response:
        print(row)
        st.header(row)