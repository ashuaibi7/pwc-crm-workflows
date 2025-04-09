import streamlit as st
from views.home import home
from views.healthie_csv_formatter import healthie_csv_formatter_page


def main():
    nav_option = st.sidebar.selectbox(
        "Navigate",
        ("Home", "Format Healthie Visits"),
    )
    if nav_option == "Home":
        home()
    elif nav_option == "Format Healthie Visits":
        healthie_csv_formatter_page()


if __name__ == "__main__":
    main()
