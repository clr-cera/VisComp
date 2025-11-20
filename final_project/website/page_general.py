import streamlit as st
import visualizations
from data import load_data

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


def render_page_general():
    st.title("Visualizações Gerais")
    st.write("Esta página contém visualizações gerais baseadas nos históricos acadêmicos dos estudantes do curso de Ciências de Computação da USP São Carlos.")
    st.write("Estas visualizações devem fornecer insights sobre tendências gerais e padrões no desempenho acadêmico e escolhas de disciplinas destes estudantes.")
    grades_with_students, students, grades = load_data()
    show_visualizations(grades_with_students, students, grades)