import streamlit as st
from streamlit_gsheets import GSheetsConnection

#Dado Locado

def show_export():
    st.header("Relatório da Assembleia Geral")

    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read()

    # Print results.
    st.write(df)