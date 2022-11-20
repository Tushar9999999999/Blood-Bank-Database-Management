import pandas as pd
import streamlit as st
from database import b_view_all_data, b_edit_blood_data, b_view_only_blood_id, b_get_blood
from database import bb_view_all_data, bb_edit_blood_data, bb_view_only_blood_id, bb_get_blood
from database import bbm_view_all_data, bbm_edit_blood_data, bbm_view_only_blood_id, bbm_get_blood
from database import bs_view_all_data, bs_edit_blood_data, bs_view_only_blood_id, bs_get_blood
from database import d_view_all_data, d_edit_blood_data, d_view_only_blood_id, d_get_blood
from database import h_view_all_data, h_edit_blood_data, h_view_only_blood_id, h_get_blood
from database import r_view_all_data, r_edit_blood_data, r_view_only_blood_id, r_get_blood

# Blood

def b_update():
    result = b_view_all_data()
    df = pd.DataFrame(result, columns=['blood_id', 'blood_type', 'd_id', 'b_no'])
    with st.expander("Current Blood"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in b_view_only_blood_id()]
    selected_blood = st.selectbox("Select blood to Edit", list_of_blood)
    selected_result = b_get_blood(selected_blood)

    if selected_result:
        blood_id = selected_result[0][0]
        blood_type = selected_result[0][1]
        d_id = selected_result[0][2]
        b_no = selected_result[0][3]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_blood_id = st.text_input("blood_id:", blood_id)
            new_blood_type = st.text_input("blood_type:", blood_type)
        with col2:
            new_d_id = st.text_input("d_id:", d_id)
            new_b_no = st.text_input("b_no:", b_no)
        if st.button("Update Blood"):
            b_edit_blood_data(new_blood_id, new_blood_type, new_d_id, new_b_no, blood_id, blood_type, d_id, b_no)
            st.success("Successfully updated: {} to :{}".format(blood_id, new_blood_id))

    result2 = b_view_all_data()
    df2 = pd.DataFrame(result2, columns=['blood_id', 'blood_type', 'd_id', 'b_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Blood Bank

def bb_update():
    result = bb_view_all_data()
    df = pd.DataFrame(result, columns=['b_no', 'orders', 'type', 'qty', 'emp_id', 'hosp_name'])
    with st.expander("Current Blood Bank"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in bb_view_only_blood_id()]
    selected_blood = st.selectbox("Select Blood Bank to Edit", list_of_blood)
    selected_result = bb_get_blood(selected_blood)

    if selected_result:
        b_no = selected_result[0][0]
        orders = selected_result[0][1]
        type = selected_result[0][2]
        qty = selected_result[0][3]
        emp_id = selected_result[0][4]
        hosp_name = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_b_no = st.text_input("b_no:", b_no)
            new_orders = st.text_input("orders:", orders)
            new_type = st.text_input("type:", type)
        with col2:
            new_qty = st.number_input("qty:", qty)
            new_emp_id = st.text_input("emp_id:", emp_id)
            new_hosp_name = st.text_input("hosp_name:", hosp_name)
        if st.button("Update Blood Bank"):
            bb_edit_blood_data(new_b_no, new_orders, new_type, new_qty, new_emp_id, new_hosp_name, b_no, orders, type, qty, emp_id, hosp_name)
            st.success("Successfully Updated Blood Bank: {} to :{}".format(b_no, new_b_no))

    result2 = bb_view_all_data()
    df2 = pd.DataFrame(result2, columns=['b_no', 'orders', 'type', 'qty', 'emp_id', 'hosp_name'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Blood Bank Manager

def bbm_update():
    result = bbm_view_all_data()
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'email_id', 'phno', 'b_no'])
    with st.expander("Current Blood Bank Manager"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in bbm_view_only_blood_id()]
    selected_blood = st.selectbox("Select Blood Bank Manager to Edit", list_of_blood)
    selected_result = bbm_get_blood(selected_blood)

    if selected_result:
        emp_id = selected_result[0][0]
        name = selected_result[0][1]
        email_id = selected_result[0][2]
        phno = selected_result[0][3]
        b_no = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_emp_id = st.text_input("emp_id:", emp_id)
            new_name = st.text_input("name:", name)
            new_email_id = st.text_input("email_id:", email_id)
        with col2:
            new_phno = st.text_input("phno:", phno)
            new_b_no = st.text_input("b_no:", b_no)

        if st.button("Update Blood Bank Manager"):
            bbm_edit_blood_data(new_emp_id, new_name, new_email_id, new_phno, new_b_no, emp_id, name, email_id, phno, b_no)
            st.success("Successfully Updated Blood Bank Manager: {} to :{}".format(emp_id, new_emp_id))


    result2 = bbm_view_all_data()
    df2 = pd.DataFrame(result2, columns=['emp_id', 'name', 'email_id', 'phno', 'b_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Blood Stock

def bs_update():
    result = bs_view_all_data()
    df = pd.DataFrame(result, columns=['blood_id', 'stock_qty', 'cost'])
    with st.expander("Current Blood Stock"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in bs_view_only_blood_id()]
    selected_blood = st.selectbox("Select Blood Stock to Edit", list_of_blood)
    selected_result = bs_get_blood(selected_blood)

    if selected_result:
        blood_id = selected_result[0][0]
        stock_qty = selected_result[0][1]
        cost = selected_result[0][2]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_blood_id = st.text_input("blood_id:", blood_id)
        with col2:
            new_stock_qty = st.number_input("stock_qty:", stock_qty)
            new_cost = st.number_input("cost:", cost)
        if st.button("Update Blood Stock"):
            bs_edit_blood_data(new_blood_id, new_stock_qty, new_cost, blood_id, stock_qty, cost)
            st.success("Successfully Updated Blood Stock: {} to :{}".format(blood_id, new_blood_id))

    result2 = bs_view_all_data()
    df2 = pd.DataFrame(result2, columns=['blood_id', 'stock_qty', 'cost'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Donor

def d_update():
    result = d_view_all_data()
    df = pd.DataFrame(result, columns=['d_id', 'name', 'gender', 'age', 'address', 'state', 'pincode', 'phno', 'emp_id'])
    with st.expander("Current Donor"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in d_view_only_blood_id()]
    selected_blood = st.selectbox("Select donor to Edit", list_of_blood)
    selected_result = d_get_blood(selected_blood)

    if selected_result:
        d_id = selected_result[0][0]
        name = selected_result[0][1]
        gender = selected_result[0][2]
        age = selected_result[0][3]
        address = selected_result[0][4]
        state = selected_result[0][5]
        pincode = selected_result[0][6]
        phno = selected_result[0][7]
        emp_id = selected_result[0][8]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_d_id = st.text_input("d_id:", d_id)
            new_name = st.text_input("name:", name)
            new_gender = st.text_input("gender:", gender)
            new_age = st.text_input("age:", age)
            new_address = st.text_input("address:", address)
        with col2:
            new_state = st.text_input("state:", state)
            new_pincode = st.text_input("pincode:", pincode)
            new_phno = st.text_input("phno:", phno)
            new_emp_id = st.text_input("emp_id:", emp_id)

        if st.button("Update Donor"):
            d_edit_blood_data(new_d_id, new_name, new_gender, new_age, new_address, new_state, new_pincode, new_phno, new_emp_id, d_id, name, gender, age, address, state, pincode, phno, emp_id)
            st.success("Successfully updated: {} to :{}".format(d_id, new_d_id))

    result2 = d_view_all_data()
    df2 = pd.DataFrame(result2, columns=['d_id', 'name', 'gender', 'age', 'address', 'state', 'pincode', 'phno', 'emp_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Hospital

def h_update():
    result = h_view_all_data()
    df = pd.DataFrame(result, columns=['name', 'address', 'phno', 'b_no', 'b_no_2'])
    with st.expander("Current Hospital"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in h_view_only_blood_id()]
    selected_blood = st.selectbox("Select hospital to Edit", list_of_blood)
    selected_result = h_get_blood(selected_blood)

    if selected_result:
        name = selected_result[0][0]
        address = selected_result[0][1]
        phno = selected_result[0][2]
        b_no = selected_result[0][3]
        b_no_2 = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_name = st.text_input("name:", name)
            new_address = st.text_input("address:", address)
        with col2:
            new_phno = st.text_input("phno:", phno)
            new_b_no = st.text_input("b_no:", b_no)
            new_b_no_2 = st.text_input("b_no_2:", b_no_2)

        if st.button("Update Hospital"):
            h_edit_blood_data(new_name, new_address, new_phno, new_b_no, new_b_no_2, name, address, phno, b_no, b_no_2)
            st.success("Successfully updated: {} to :{}".format(name, new_name))

    result2 = h_view_all_data()
    df2 = pd.DataFrame(result2, columns=['name', 'address', 'phno', 'b_no', 'b_no_2'])
    with st.expander("Updated data"):
        st.dataframe(df2)

# Receptionist

def r_update():
    result = r_view_all_data()
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'address', 'phno', 'b_no'])
    with st.expander("Current Receptionist"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in r_view_only_blood_id()]
    selected_blood = st.selectbox("Select Receptionist to Edit", list_of_blood)
    selected_result = r_get_blood(selected_blood)

    if selected_result:
        emp_id = selected_result[0][0]
        name = selected_result[0][1]
        address = selected_result[0][2]
        phno = selected_result[0][3]
        b_no = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_emp_id = st.text_input("emp_id:", emp_id)
            new_name = st.text_input("name:", name)
            new_address = st.text_input("address:", address)
        with col2:
            new_phno = st.text_input("phno:", phno)
            new_b_no = st.text_input("b_no:", b_no)

        if st.button("Update Receptionist"):
            r_edit_blood_data(new_emp_id, new_name, new_address, new_phno, new_b_no, emp_id, name, address, phno, b_no)
            st.success("Successfully updated: {} to :{}".format(emp_id, new_emp_id))

    result2 = r_view_all_data()
    df2 = pd.DataFrame(result2, columns=['emp_id', 'name', 'address', 'phno', 'b_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)