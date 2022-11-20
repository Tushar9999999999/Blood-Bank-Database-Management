import streamlit as st
from home import home
from terminal import terminal
from PIL import Image

def page():
    st.subheader("Welcome to Tushar's Blood Bank Database Project")
    image = Image.open('blood_bank_pic.gif')
    st.image(image, caption='Blood Bank')

def main():
    st.set_page_config(
        page_title="Blood Bank",
        page_icon="💉",
    )
    st.title("Blood Bank")

    menu = ["Main Page", "Terminal", "Tables"]
    choice = st.sidebar.selectbox("Nav", menu)

    if choice == "Main Page":
        page()

    elif choice == "Terminal":
        st.subheader("Terminal")
        terminal()

    elif choice == "Tables":
        home()

    else:
        st.subheader("Hi")

if __name__ == '__main__':
	main()