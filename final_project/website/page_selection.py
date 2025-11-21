import streamlit as st
import visualizations
from data import load_data, load_dependencies

def show_visualizations(grades_with_students, students, grades, dependencies_df, edge_list):
    class_dep_network = visualizations.class_dependencies_network(dependencies_df, edge_list)
    
    # Capture selection events
    selected = st.plotly_chart(class_dep_network, on_select="rerun", selection_mode=["points", "box", "lasso"])
    
    # Display selected points information
    if selected and selected.selection and selected.selection.points:
        st.subheader("Disciplinas Selecionadas")
        selected_codes = parse_selected_codes(selected)

        st.write("Análises de contagem Disciplinas Selecionadas:")
        department_count_fig = visualizations.department_count_per_point_selection(selected_codes)
        st.plotly_chart(department_count_fig)
        semester_count_fig = visualizations.semester_count_per_point_selection(selected_codes, dependencies_df)
        st.plotly_chart(semester_count_fig)

        st.write("Análises de notas nas Disciplinas Selecionadas:")
        department_grade_fig = visualizations.average_grades_bar_plot_by_department_by_selection(selected_codes, grades_with_students)
        st.plotly_chart(department_grade_fig)
        semester_grade_fig = visualizations.average_grades_bar_plot_by_semester_by_selection(selected_codes, grades_with_students, dependencies_df)
        st.plotly_chart(semester_grade_fig)
        
def parse_selected_codes(selected):
    selected_codes = []
    for point in selected.selection.points:
        hover_text = point.get('hovertext', point.get('text', ''))
        # Parse "Código: SCC0221" from hover text
        if 'Código:' in hover_text:
            code = hover_text.split('Código:')[1].split('<br>')[0].strip()
            selected_codes.append(code)
    return selected_codes

def render_page_selection():
    st.title("Visualizações com Seleção de Disciplinas")
    st.write("Esta página contém uma visualização das dependências entre as disciplinas do curso de Ciências de Computação da USP São Carlos.")
    st.write("A visualização representa as disciplinas como nós e as dependências como arestas, permitindo uma compreensão clara das relações entre as disciplinas.")
    st.write("Você pode interagir com o gráfico selecionando disciplinas específicas para ver mais detalhes sobre elas.")
    grades_with_students, students, grades = load_data()
    dependencies_df, edge_list = load_dependencies()
    show_visualizations(grades_with_students, students, grades, dependencies_df, edge_list)
