import streamlit as st
from export.page import show_export
from genres.page import show_genres

def main():
    st.title("Dashboard Financeiro - IBF")

    menu_option = st.sidebar.selectbox(
        "Selecione uma opção", 
        ["Visão Geral", "Relatório Assembleia Geral", "Mais Informações", "Gêneros de Filmes",]
        )  
    
    if menu_option == "Visão Geral":
        st.header("Visão Geral da IBF")
    
    if menu_option == "Relatório Assembleia Geral":
        show_export()
    
    if menu_option == "Mais Informações":
        st.header("Outras Informações Relevantes da IBF")
    
    if menu_option == "Gêneros de Filmes":
        show_genres()


if __name__ == '__main__':
    main()