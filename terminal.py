import streamlit as st
from database import term_q
import pandas as pd

def terminal():
    query = st.text_input("SQL query:")
    if st.button("Run query"):
        result = term_q(query)
        df = pd.DataFrame(result)
        st.dataframe(df)