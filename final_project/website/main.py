import streamlit as st
import page_general

def main_page():
    st.title("Academic Record Visualization")
    st.write("This application offer visualizations from the academic records of 5 students from the Computer Science course in USP São Carlos.")

if __name__ == "__main__":

    pages = [st.Page(main_page, title="Home"),
             st.Page(page_general.render_page, title="General Visualizations")]
    pg = st.navigation(pages, position='top')
    pg.run()
