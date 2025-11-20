import pandas as pd

def load_data():
    students = pd.read_csv("data/students.csv")
    grades = pd.read_csv("data/final_table.csv")
    grades = grades.assign(
        Departament=grades['Sigla'].str.slice(0, 3),
        IdEstudante=grades['student_id']
        )
    grades_with_students = grades.merge(students, on='IdEstudante', how='left')
    return grades_with_students, students, grades

def load_dependencies():
    dependencies_df = pd.read_csv("data/dependencies.csv")
    edge_list = pd.read_csv("data/dependencies_edge_list.csv")
    return dependencies_df, edge_list