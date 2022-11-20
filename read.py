import pandas as pd
import streamlit as st
import plotly.express as px
from database import b_view_all_data, bb_view_all_data, bbm_view_all_data, bs_view_all_data, d_view_all_data, \
    h_view_all_data, r_view_all_data

# Blood

def b_read():
    result = b_view_all_data()
    df = pd.DataFrame(result, columns=['blood_id', 'blood_type', 'd_id', 'b_no'])
    with st.expander("View all Blood"):
        st.dataframe(df)
    with st.expander("Blood details"):
        blood_df = df['blood_type'].value_counts().to_frame()
        blood_df = blood_df.reset_index()
        st.dataframe(blood_df)
        p1 = px.pie(blood_df, names='index', values='blood_type')
        st.plotly_chart(p1)

# Blood Bank

def bb_read():
    result = bb_view_all_data()
    df = pd.DataFrame(result, columns=['b_no', 'orders', 'type', 'qty', 'emp_id', 'hosp_name'])
    with st.expander("View all Blood Banks"):
        st.dataframe(df)

#Blood Bank Manager

def bbm_read():
    result = bbm_view_all_data()
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'email_id', 'phno', 'b_no'])
    with st.expander("View all Blood Bank Managers"):
        st.dataframe(df)

#Blood Stock

def bs_read():
    result = bs_view_all_data()
    df = pd.DataFrame(result, columns=['blood_id', 'stock_qty', 'cost'])
    with st.expander("View all Blood Stock"):
        st.dataframe(df)

# Donor

def d_read():
    result = d_view_all_data()
    df = pd.DataFrame(result, columns=['d_id', 'name', 'gender', 'age', 'address', 'state', 'pincode', 'phno', 'emp_id'])
    with st.expander("View all Donors"):
        st.dataframe(df)

# Hospital

def h_read():
    result = h_view_all_data()
    df = pd.DataFrame(result, columns=['name', 'address', 'phno', 'b_no', 'b_no_2'])
    with st.expander("View all Hospitals"):
        st.dataframe(df)

# Receptionist

def r_read():
    result = r_view_all_data()
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'address', 'phno', 'b_no'])
    with st.expander("View all Receptionists"):
        st.dataframe(df)