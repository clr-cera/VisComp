import streamlit as st
import page_selection
import page_general

def main_page():
    st.title("Visualização de Histórico Acadêmico")
    st.write("Esta aplicação oferece visualizações dos históricos acadêmicos de 5 estudantes do curso de Ciências de Computação da USP São Carlos.")
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("https://icmc.usp.br/imprensa/default.jpg", width=400)
    with left_co:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Ferris_trans_flag_pride.jpg/500px-Ferris_trans_flag_pride.jpg", width=400)
    with last_co:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Ferris_trans_flag_pride.jpg/500px-Ferris_trans_flag_pride.jpg", width=400)


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
