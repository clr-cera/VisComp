import streamlit as st
from data import load_data
from visualizations import average_grade_per_department

if __name__ == "__main__":
    grades_with_students = load_data()
    st.title("Academic Record Visualization")
    st.write("This application offer visualizations from the academic records of 5 students from the Computer Science course in USP São Carlos.")

    plot = average_grade_per_department(grades_with_students)
    st.plotly_chart(plot)