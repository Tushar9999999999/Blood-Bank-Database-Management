import streamlit as st
from create import b_create, bb_create, bbm_create, bs_create, d_create, h_create, r_create
from delete import b_delete, bb_delete, bbm_delete, bs_delete, d_delete, h_delete, r_delete
from read import b_read, bb_read, bbm_read, bs_read, d_read, h_read, r_read
from update import b_update, bb_update, bbm_update, bs_update, d_update, h_update, r_update

# Blood

def b_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Blood Details:")
        b_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        b_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        b_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        b_delete()

    else:
        st.subheader("About Tables")

# Blood Bank

def bb_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Blood Bank Details:")
        bb_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        bb_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        bb_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        bb_delete()

    else:
        st.subheader("About Tables")

# Blood Bank Manager

def bbm_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Blood Bank Manager Details:")
        bbm_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        bbm_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        bbm_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        bbm_delete()

    else:
        st.subheader("About Tables")

# Blood Stock

def bs_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Blood Stock Details:")
        bs_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        bs_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        bs_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        bs_delete()

    else:
        st.subheader("About Tables")

# Donor

def d_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Donor Details:")
        d_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        d_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        d_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        d_delete()

    else:
        st.subheader("About Tables")

# Hospital

def h_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Hospital Details:")
        h_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        h_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        h_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        h_delete()

    else:
        st.subheader("About Tables")

# Receptionist

def r_app():
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add":
        st.subheader("Enter Receptionist Details:")
        r_create()

    elif choice == "View":
        st.subheader("View Created Tables")
        r_read()

    elif choice == "Edit":
        st.subheader("Update Created Tables")
        r_update()

    elif choice == "Remove":
        st.subheader("Delete Created Tables")
        r_delete()

    else:
        st.subheader("About Tables")