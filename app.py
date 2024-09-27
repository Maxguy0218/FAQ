import streamlit as st
import pandas as pd

# Title of the page
st.title("FAQ")


@st.cache
def load_data():
    df = pd.read_csv('faq.csv')
    return df

# Load the FAQs from the CSV file
df = load_data()

# Display FAQs dynamically using collapsible sections
for index, row in df.iterrows():
    with st.expander(row['QUESTIONS']):
        st.write(row['ANSWER'])
