import streamlit as st
import mysql.connector

# Database connection function
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="0070100",  # Replace with your MySQL password
        database="student_data"
    )
    return connection

# Function to insert data into the database
def insert_student_data(name, roll, dept, year, age, gender, email):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        query = """INSERT INTO students (name, roll, dept, year, age, gender, email)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (name, roll, dept, year, age, gender, email))
        connection.commit()
        st.success("Student data saved successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Streamlit form
st.title("Student Data Collection Form")

with st.form("student_form"):
    name = st.text_input("Name")
    roll = st.number_input("Roll Number", step=1)
    dept = st.text_input("Department")
    year = st.number_input("Year of Study", step=1, min_value=1, max_value=5)
    age = st.number_input("Age", step=1, min_value=16, max_value=100)
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    if name and roll and dept and year and age and gender and email:
        insert_student_data(name, roll, dept, year, age, gender, email)
    else:
        st.error("Please fill out all fields.")
