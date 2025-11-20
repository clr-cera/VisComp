import streamlit as st
from data import load_data
import visualizations



def show_visualizations(grades_with_students, students, grades):
    # Show all visualizations available
    avg_per_dpt = visualizations.average_grade_per_department(grades_with_students)
    st.plotly_chart(avg_per_dpt)

    avg_grade_rel_sem = visualizations.average_grade_per_relative_semester(grades_with_students)
    st.plotly_chart(avg_grade_rel_sem)
    
    avg_au_rel_sem = visualizations.average_au_per_relative_semester(grades_with_students)
    st.plotly_chart(avg_au_rel_sem)    
    
    low_freq_disciplines = visualizations.disciplines_with_lowest_frequency(grades_with_students)
    st.plotly_chart(low_freq_disciplines)

    grades_scatter_credits = visualizations.grades_scatter_by_credits(grades_with_students)
    st.plotly_chart(grades_scatter_credits)

    dept_count_per_student = visualizations.department_count_per_student(grades_with_students)
    st.plotly_chart(dept_count_per_student)

    freq_grade_scatter = visualizations.frequency_vs_grade_scatter(grades_with_students)
    st.plotly_chart(freq_grade_scatter)

    dept_contribution = visualizations.department_contribution_to_average(grades_with_students, students)
    st.plotly_chart(dept_contribution)









if __name__ == "__main__":
    grades_with_students, students, grades = load_data()
    
    st.title("Academic Record Visualization")
    st.write("This application offer visualizations from the academic records of 5 students from the Computer Science course in USP São Carlos.")

    show_visualizations(grades_with_students, students, grades)