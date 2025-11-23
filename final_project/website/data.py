from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2] / "data"


def _read_data_csv(filename: str) -> pd.DataFrame:
    file_path = BASE_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {file_path}")
    return pd.read_csv(file_path)


def load_data():
    students = _read_data_csv("students.csv")
    grades = _read_data_csv("final_table.csv")
    grades = grades.assign(
        Departament=grades['Sigla'].str.slice(0, 3),
        IdEstudante=grades['student_id']
        )
    grades_with_students = grades.merge(students, on='IdEstudante', how='left')
    return grades_with_students, students, grades


def load_dependencies():
    dependencies_df = _read_data_csv("dependencies.csv")
    edge_list = _read_data_csv("dependencies_edge_list.csv")
    return dependencies_df, edge_list
