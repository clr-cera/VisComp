import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def average_grade_per_department(grades_with_students):

    dept_avg = grades_with_students.groupby('Departament', as_index=False)['NOTA'].mean()
    plot = px.bar(dept_avg, x='Departament', y='NOTA', title='Average Grade per Department', color='Departament')
    plot.update_xaxes(type='category')
    return plot
def average_grade_per_relative_semester(grades_with_students):
    # Add Ano and Semestre columns
    grades_df = grades_with_students.copy()
    grades_df['Ano'] = grades_df['Ano/Semestre'].str.split('/').str[0].astype(int)
    grades_df['Semestre'] = grades_df['Ano/Semestre'].str.split('/').str[1].astype(int)
    grades_df['RelSemester'] = (grades_df['Ano'] - grades_df['AnoIngresso']) * 2 + grades_df['Semestre']
    
    # Filter and aggregate
    average_grades = grades_df[grades_df['RelSemester'] < 6].groupby('RelSemester', as_index=False)['NOTA'].mean()
    average_grades.columns = ['RelSemester', 'AverageGrade']
    
    fig = px.line(average_grades, x='RelSemester', y='AverageGrade', 
                  title='Média das Notas por Semestre Relativo')
    fig.update_xaxes(dtick=1)
    return fig

def average_au_per_relative_semester(grades_with_students):
    # Add Ano, Semestre, and RelSemester columns
    grades_df = grades_with_students.copy()
    grades_df['Ano'] = grades_df['Ano/Semestre'].str.split('/').str[0].astype(int)
    grades_df['Semestre'] = grades_df['Ano/Semestre'].str.split('/').str[1].astype(int)
    grades_df['RelSemester'] = (grades_df['Ano'] - grades_df['AnoIngresso']) * 2 + grades_df['Semestre']
    
    # Sum AU per student per semester
    au_per_student_semester = grades_df.groupby(['IdEstudante', 'RelSemester'], as_index=False)['AU'].sum()
    au_per_student_semester.columns = ['IdEstudante', 'RelSemester', 'TotalAU']
    
    # Average AU per semester
    average_au = au_per_student_semester[au_per_student_semester['RelSemester'] < 6].groupby('RelSemester', as_index=False)['TotalAU'].mean()
    average_au.columns = ['RelSemester', 'AverageAU']
    
    fig = px.line(average_au, x='RelSemester', y='AverageAU', 
                  title='Média de AU por Semestre Relativo')
    fig.update_xaxes(dtick=1)
    return fig

def disciplines_with_lowest_frequency(grades_with_students):
    # Add RelSemester
    grades_df = grades_with_students.copy()
    grades_df['Ano'] = grades_df['Ano/Semestre'].str.split('/').str[0].astype(int)
    grades_df['Semestre'] = grades_df['Ano/Semestre'].str.split('/').str[1].astype(int)
    grades_df['RelSemester'] = (grades_df['Ano'] - grades_df['AnoIngresso']) * 2 + grades_df['Semestre']
    
    # Filter and aggregate
    name_frequency = grades_df[grades_df['RelSemester'] < 6].groupby('Nome', as_index=False)['FREQ'].mean()
    name_frequency.columns = ['Nome', 'AverageFrequency']
    name_frequency_sorted = name_frequency.sort_values('AverageFrequency').head(10)
    
    fig = px.bar(name_frequency_sorted, x='AverageFrequency', y='Nome', 
                 title='Top 10 Disciplinas com Menor Frequência', 
                 color='AverageFrequency', orientation='h')
    return fig

def grades_scatter_by_credits(grades_with_students):
    # Add RelSemester
    grades_df = grades_with_students.copy()
    grades_df['Ano'] = grades_df['Ano/Semestre'].str.split('/').str[0].astype(int)
    grades_df['Semestre'] = grades_df['Ano/Semestre'].str.split('/').str[1].astype(int)
    grades_df['RelSemester'] = (grades_df['Ano'] - grades_df['AnoIngresso']) * 2 + grades_df['Semestre']
    
    # Filter
    filtered_df = grades_df[grades_df['RelSemester'] < 6]
    
    fig = px.scatter(filtered_df, x='AU+TR', y='NOTA', 
                     title='Dispersão de Notas por AU e TR')
    return fig

def department_count_per_student(grades_with_students):
    dept_counts = grades_with_students.groupby(['IdEstudante', 'Departament']).size().reset_index(name='Count')
    dept_counts = dept_counts.sort_values(['IdEstudante', 'Count'])
    
    fig = px.bar(dept_counts, x='IdEstudante', y='Count', color='Departament', 
                 title='Contagem de Departamentos por Estudante', 
                 barmode='group', orientation='v')
    return fig


def frequency_vs_grade_scatter(grades_with_students):
    """
    Scatter plot of frequency vs grade with department color coding.
    Allows identification of correlation between frequency and grade.
    """
    fig = px.scatter(grades_with_students, x="FREQ", y="NOTA", color="Departament", 
                     hover_data=["Nome", "FREQ", "NOTA"], 
                     title="Scatter Plot de Frequência x Nota")
    return fig

def department_contribution_to_average(grades_with_students, students):
    """
    Stacked area chart showing each department's contribution to the average grade per semester.
    Interactive dropdown allows switching between different students.
    
    Parameters:
    - grades_with_students: DataFrame with grades joined with student info
    - students: DataFrame with student information (must have IdEstudante as index)
    """
    fig = go.Figure()
    
    all_semesters = sorted(grades_with_students["Ano/Semestre"].unique())
    trace_count_per_student = []
    student_semester_ranges = []  # Store the semester range for each student
    
    for student in students.index:
        semesters = []
        averages = []
        student_df = grades_with_students[grades_with_students["IdEstudante"] == student]
        
        # Get the actual semesters this student has data for
        student_semesters = sorted(student_df["Ano/Semestre"].unique())
        student_semester_ranges.append(student_semesters)
        
        for semester in all_semesters:
            student_sem_df = student_df[student_df["Ano/Semestre"] == semester]
            semesters.append(semester)
            if student_sem_df.empty:
                averages.append(None)
                continue
            sem_avgs = {}
            semester_total = 0
            for depto in student_df["Departament"].unique():
                student_sem_depto_notas = student_sem_df[student_sem_df["Departament"] == depto]["NOTA"]
                avg = student_sem_depto_notas.mean()
                count = student_sem_depto_notas.count()
                avg = avg if count != 0 else 0
                sem_avgs[depto] = (avg, count)
                semester_total += count
            sem_avgs["total"] = semester_total
            averages.append(sem_avgs)
        
        # Create traces for this student
        total_y = np.array([0.0] * len(averages), dtype=np.float64)
        for depto in student_df["Departament"].unique():
            y = list(map(lambda x: x[depto][0] * x[depto][1] / x["total"] if x is not None else 0, averages))
            total_y += np.array(y)
            
            trace = go.Scatter(
                x=semesters,
                y=y,
                mode="lines+markers",
                stackgroup="depto",
                name=depto,
                visible=(student == students.index[0])  # Only first student visible initially
            )
            fig.add_trace(trace)
        
        # Add total average line
        fig.add_trace(go.Scatter(
            x=semesters,
            y=total_y,
            mode="lines",
            name="Média do semestre",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="<b>Média total: %{y:.2f}</b><extra></extra>",
            visible=(student == students.index[0])
        ))
        
        trace_count_per_student.append(len(student_df["Departament"].unique()) + 1)
    
    # Create dropdown buttons for student selection
    buttons = []
    for i, student in enumerate(students.index):
        start_idx = sum(trace_count_per_student[:i])
        end_idx = start_idx + trace_count_per_student[i]
        
        visible = [False] * len(fig.data)
        for j in range(start_idx, end_idx):
            visible[j] = True
        
        # Get the semester range for this student
        student_sems = student_semester_ranges[i]
        xaxis_range = None
        if len(student_sems) > 0:
            # Add some padding to the range
            first_sem_idx = all_semesters.index(student_sems[0])
            last_sem_idx = all_semesters.index(student_sems[-1])
            # Set range with a bit of padding (0.5 semesters on each side)
            xaxis_range = [first_sem_idx - 0.5, last_sem_idx + 0.5]
        
        buttons.append(
            dict(
                label=f"Estudante {student}",
                method="update",
                args=[
                    {"visible": visible},
                    {
                        "title": f"Contribuição à Média por Departamento para Estudante {student}",
                        "xaxis.range": xaxis_range
                    }
                ]
            )
        )
    
    # Set initial x-axis range for the first student
    first_student_sems = student_semester_ranges[0]
    initial_xaxis_range = None
    if len(first_student_sems) > 0:
        first_sem_idx = all_semesters.index(first_student_sems[0])
        last_sem_idx = all_semesters.index(first_student_sems[-1])
        initial_xaxis_range = [first_sem_idx - 0.5, last_sem_idx + 0.5]
    
    # Add dropdown menu to layout
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=False,
                x=0.1,
                xanchor="left",
                y=1.15,
                yanchor="top",
                bgcolor="gray",
                bordercolor="gray",
                borderwidth=1
            )
        ],
        title=f"Contribuição à Média por Departamento para Estudante {students.index[0]}",
        xaxis_title="Semestre",
        yaxis_title="Média",
        hovermode='x unified'
    )
    
    # Set initial x-axis range
    if initial_xaxis_range:
        fig.update_xaxes(range=initial_xaxis_range)
    
    return fig