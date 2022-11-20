import pandas as pd
import streamlit as st
from database import b_view_all_data, b_view_only_blood_id, b_delete_data
from database import bb_view_all_data, bb_view_only_blood_id, bb_delete_data
from database import bbm_view_all_data, bbm_view_only_blood_id, bbm_delete_data
from database import bs_view_all_data, bs_view_only_blood_id, bs_delete_data
from database import d_view_all_data, d_view_only_blood_id, d_delete_data
from database import h_view_all_data, h_view_only_blood_id, h_delete_data
from database import r_view_all_data, r_view_only_blood_id, r_delete_data

# Blood

def b_delete():
    result = b_view_all_data()
    df = pd.DataFrame(result, columns=['blood_id', 'blood_type', 'd_id', 'b_no'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in b_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Blood"):
        b_delete_data(selected_blood)
        st.success("Blood has been deleted successfully")

    new_result = b_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['blood_id', 'blood_type', 'd_id', 'b_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Blood Bank

def bb_delete():
    result = bb_view_all_data()
    df = pd.DataFrame(result, columns=['b_no', 'orders', 'type', 'qty', 'emp_id', 'hosp_name'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in bb_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Blood Bank"):
        bb_delete_data(selected_blood)
        st.success("Blood Bank has been deleted successfully")

    new_result = bb_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['b_no', 'orders', 'type', 'qty', 'emp_id', 'hosp_name'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Blood Bank Manager

def bbm_delete():
    result = bbm_view_all_data()
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'email_id', 'phno', 'b_no'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in bbm_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Blood Bank Manager"):
        bbm_delete_data(selected_blood)
        st.success("Blood Bank Manager has been deleted successfully")

    new_result = bbm_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['emp_id', 'name', 'email_id', 'phno', 'b_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Blood Stock

def bs_delete():
    result = bs_view_all_data()
    df = pd.DataFrame(result, columns=['blood_id', 'stock_qty', 'cost'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in bs_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Blood Stock"):
        bs_delete_data(selected_blood)
        st.success("Blood Stock has been deleted successfully")

    new_result = bs_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['blood_id', 'stock_qty', 'cost'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Donor

def d_delete():
    result = d_view_all_data()
    df = pd.DataFrame(result, columns=['d_id', 'name', 'gender', 'age', 'address', 'state', 'pincode', 'phno', 'emp_id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in d_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Blood"):
        d_delete_data(selected_blood)
        st.success("Donor has been deleted successfully")

    new_result = d_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['d_id', 'name', 'gender', 'age', 'address', 'state', 'pincode', 'phno', 'emp_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Hospital

def h_delete():
    result = h_view_all_data()
    df = pd.DataFrame(result, columns=['name', 'address', 'phno', 'b_no', 'b_no_2'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in h_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Hospital"):
        h_delete_data(selected_blood)
        st.success("Hospital has been deleted successfully")

    new_result = h_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['name', 'address', 'phno', 'b_no', 'b_no_2'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Receptionist

def r_delete():
    result = r_view_all_data()
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'address', 'phno', 'b_no'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in r_view_only_blood_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete: {}".format(selected_blood))
    if st.button("Delete Receptionist"):
        r_delete_data(selected_blood)
        st.success("Receptionist has been deleted successfully")

    new_result = r_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['name', 'address', 'phno', 'b_no', 'b_no_2'])
    with st.expander("Updated data"):
        st.dataframe(df2)