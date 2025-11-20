import plotly.express as px

def average_grade_per_department(grades_with_students):

    dept_avg = grades_with_students.groupby('Departament', as_index=False)['NOTA'].mean()
    plot = px.bar(dept_avg, x='Departament', y='NOTA', title='Average Grade per Department', color='Departament')
    plot.update_xaxes(type='category')
    return plot