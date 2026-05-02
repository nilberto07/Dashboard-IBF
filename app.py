import streamlit as st
from export.page import show_export
from genres.page import show_genres

color = st.get_option("theme.secondaryBackgroundColor")

st.set_page_config(
    page_title="Controle Financeiro das Igrejas",
    page_icon="⛪",
    #layout="wide", #Tela cheia
    #initial_sidebar_state="expanded" #Sidebar expandida por padrão
)
st.itens_de_menu=["Visão Geral", "Relatório Assembleia Geral", "Mais Informações", "Gêneros de Filmes"]


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