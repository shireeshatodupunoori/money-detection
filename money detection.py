import streamlit as st
import re

# Function to extract money patterns
def extract_money(text):
    # Common currency formats: $, €, ₹, £ with numbers
    pattern = r'[\$\€\₹\£]\s?\d+(?:,\d{3})*(?:\.\d{1,2})?'
    matches = re.findall(pattern, text)
    return matches

# Streamlit App
st.title("💵 Money Detector from Text")

# User input
user_input = st.text_area("Enter text containing money amounts:")

# Button to trigger detection
if st.button("Detect Money"):
    found_money = extract_money(user_input)
    if found_money:
        st.success(f"Detected amounts: {', '.join(found_money)}")
    else:
        st.warning("No money amounts found in the text.")
