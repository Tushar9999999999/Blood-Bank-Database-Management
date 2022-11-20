import streamlit as st

from app import b_app, bb_app, bbm_app, bs_app, d_app, h_app, r_app
from terminal import terminal

def home():

    menu = ["Blood", "Blood_Bank", "Blood_Bank_Manager", "Blood_Stock", "Donor", "Hospital", "Receptionist"]
    choice = st.sidebar.selectbox("Tables", menu)

    if choice == "Blood":
        st.subheader("Blood Table")
        b_app()

    elif choice == "Blood_Bank":
        st.subheader("Blood Bank Table")
        bb_app()

    elif choice == "Blood_Bank_Manager":
        st.subheader("Blood Bank Manager Table")
        bbm_app()

    elif choice == "Blood_Stock":
        st.subheader("Blood Stock Table")
        bs_app()

    elif choice == "Donor":
        st.subheader("Donor Table")
        d_app()

    elif choice == "Hospital":
        st.subheader("Hospital Table")
        h_app()

    elif choice == "Receptionist":
        st.subheader("Receptionist")
        r_app()

    else:
        st.subheader("About Tables")
