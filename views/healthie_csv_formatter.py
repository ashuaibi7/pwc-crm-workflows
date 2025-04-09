import streamlit as st
import pandas as pd

from scripts.process_visit_csv import process_visit_csv


def healthie_csv_formatter_page():
    st.header("Healthie CSV Formatter")
    st.write(
        "Upload the Healthie CSV file for last week appointments."
        "This will format the data to easily import into the Notion Visits table."
    )

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            pass
            df = pd.read_csv(uploaded_file)
            st.subheader("Original CSV Preview")
            st.dataframe(df.head())

            processed_df = process_visit_csv(df)
            st.subheader("Processed CSV Preview")
            st.dataframe(processed_df.head())

            csv_data = processed_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Formatted CSV",
                data=csv_data,
                file_name="formatted_healthie.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
