import streamlit as st
from database import b_add_data, bb_add_data, bbm_add_data, bs_add_data, d_add_data, h_add_data

#Blood

def b_create():
    col1, col2 = st.columns(2)
    with col1:
        blood_id = st.text_input("blood_id:")
        blood_type = st.text_input("blood_type:")
    with col2:
        d_id = st.text_input("d_id:")
        b_no = st.text_input("b_no:")
    if st.button("Add Blood"):
        b_add_data(blood_id, blood_type, d_id, b_no)
        st.success("Successfully added Blood: {}".format(blood_id))

#Blood Bank

def bb_create():
    col1, col2 = st.columns(2)
    with col1:
        b_no = st.text_input("b_no:")
        orders = st.text_input("orders:")
        type = st.text_input("type:")
    with col2:
        qty = st.number_input("qty:", min_value=0)
        emp_id = st.text_input("emp_id:")
        hosp_name = st.text_input("hosp_name:")

    if st.button("Add Blood Bank"):
        bb_add_data(b_no, orders, type, qty, emp_id, hosp_name)
        st.success("Successfully Added Blood Bank: {}".format(b_no))

# Blood Bank Manager

def bbm_create():
    col1, col2 = st.columns(2)
    with col1:
        emp_id = st.text_input("emp_id:")
        name = st.text_input("name:")
        email_id = st.text_input("email_id:")
    with col2:
        phno = st.text_input("phno:")
        b_no = st.text_input("b_no:")

    if st.button("Add Blood Bank Manager"):
        bbm_add_data(emp_id, name, email_id, phno, b_no)
        st.success("Successfully Added Blood Bank Manager: {}".format(emp_id))

#Blood Stock

def bs_create():
    col1, col2 = st.columns(2)
    with col1:
        blood_id = st.text_input("blood_id:")
    with col2:
        stock_qty = st.number_input("stock_qty:", min_value=0)
        cost = st.number_input("cost:", min_value=0.0, format='%.2f')
    if st.button("Add Blood Stock"):
        bs_add_data(blood_id, stock_qty, cost)
        st.success("Successfully added Blood Stock: {}".format(blood_id))

#Donor

def d_create():
    col1, col2 = st.columns(2)
    with col1:
        d_id = st.text_input("d_id:")
        name = st.text_input("name:")
        gender = st.text_input("gender:")
        age = st.number_input("age:", min_value=0)
        address = st.text_input("address:")
    with col2:
        state = st.text_input("state:")
        pincode = st.text_input("pincode:")
        phno = st.text_input("phno:")
        emp_id = st.text_input("emp_id:")

    if st.button("Add Donor"):
        d_add_data(d_id, name, gender, age, address, state, pincode, phno, emp_id)
        st.success("Successfully added Donor: {}".format(d_id))

# Hospital

def h_create():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("name:")
        address = st.text_input("address:")
    with col2:
        phno = st.text_input("phno:")
        b_no = st.text_input("b_no:")
        b_no_2 = st.text_input("b_no_2:")
    if st.button("Add Hospital"):
        h_add_data(name, address, phno, b_no, b_no_2)
        st.success("Successfully added Hospital: {}".format(name))

# Receptionist

def r_create():
    col1, col2 = st.columns(2)
    with col1:
        emp_id = st.text_input("emp_id:")
        name = st.text_input("name:")
        address = st.text_input("address:")
    with col2:
        phno = st.text_input("phno:")
        b_no = st.text_input("b_no:")

    if st.button("Add Receptionist"):
        h_add_data(emp_id, name, address, phno, b_no)
        st.success("Successfully added Receptionist: {}".format(emp_id))