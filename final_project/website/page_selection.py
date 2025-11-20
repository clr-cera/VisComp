import streamlit as st
import visualizations
from data import load_data, load_dependencies

def show_visualizations(grades_with_students, students, grades, dependencies_df, edge_list):
    class_dep_network = visualizations.class_dependencies_network(dependencies_df, edge_list)
    st.plotly_chart(class_dep_network)

def render_page_selection():
    st.title("Visualizações de Dependências de Disciplinas")
    st.write("Esta página contém uma visualização das dependências entre as disciplinas do curso de Ciências de Computação da USP São Carlos.")
    st.write("A visualização representa as disciplinas como nós e as dependências como arestas, permitindo uma compreensão clara das relações entre as disciplinas.")
    grades_with_students, students, grades = load_data()
    dependencies_df, edge_list = load_dependencies()
    show_visualizations(grades_with_students, students, grades, dependencies_df, edge_list)
