import streamlit as st
import page_general

def main_page():
    st.title("Academic Record Visualization")
    st.write("This application offer visualizations from the academic records of 5 students from the Computer Science course in USP São Carlos.")
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("https://icmc.usp.br/imprensa/default.jpg", width=400)
    with left_co:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Ferris_trans_flag_pride.jpg/500px-Ferris_trans_flag_pride.jpg", width=400)
    with last_co:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Ferris_trans_flag_pride.jpg/500px-Ferris_trans_flag_pride.jpg", width=400)

if __name__ == "__main__":

    pages = [st.Page(main_page, title="Home"),
             st.Page(page_general.render_page, title="General Visualizations")]
    pg = st.navigation(pages, position='top')
    pg.run()
