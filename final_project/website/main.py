import streamlit as st
import page_selection
import page_general

st.set_page_config(page_title="Visualização de Histórico Acadêmico", layout="centered")

# Slightly widen the content area while keeping it centered
st.markdown(
    """
    <style>
        .block-container {
            max-width: 1100px;
            padding-top: 1.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def main_page():
    st.title("Visualização de Histórico Acadêmico")
    st.write("Esta aplicação oferece visualizações dos históricos acadêmicos de 5 estudantes do curso de Ciências de Computação da USP São Carlos.")
    st.write("Use o Header superior para acessar as visualizações da página:")    
    st.markdown(
        """
        - Home: introdução rápida da aplicação.
        - Visualizações Gerais: gráficos com propósitos gerais utilizados no projeto.
        - Visualizações com Seleção: Visualização da disciplinas e suas dependencias, com mecanismos de interação.
        - Autores: conheça a equipe do projeto.
        """
    )
    cent_co = st.columns(1)[0]
    with cent_co:
        st.image("https://icmc.usp.br/imprensa/default.jpg", width=800)

def authors_page():
    st.title("Autores")
    st.write("Este projeto foi desenvolvido com muito carinho por:")
    st.markdown("""
    - Clara Ernesto de Carvalho - 14559479
    - Felipe Carneiro Machado - 14569373  
    - Renan Parpinelli Scarpin - 14712188  
    - Gabriel Barbosa dos Santos - 14613991  
    - Lourenço de Salles Roselino - 11796805
                """)

    st.write("Agradecemos a todos que contribuíram para a realização deste projeto!")
    st.markdown(""" 
                - Instituto de Ciências Matemáticas e de Computação - USP São Carlos
                - Prof. Dr. Jean R. Ponciano - SCC0252 / SCC5836 – Visualização Computacional – 2025/2
                """)
    st.write("E claro, a você que está utilizando nossa aplicação!")
    st.image("https://cdn-5a6cb102f911c811e474f1cd.closte.com/wp-content/uploads/2017/04/How-To-Make-A-Pizza-Pie-Chart.png", width=400)
    

if __name__ == "__main__":

    pages = [st.Page(main_page, title="Home"),
             st.Page(page_general.render_page_general, title="Visualizações Gerais"),
             st.Page(page_selection.render_page_selection, title="Visualizações com Seleção"),
             st.Page(authors_page, title="Autores")
            ]
    pg = st.navigation(pages, position='top')
    pg.run()
