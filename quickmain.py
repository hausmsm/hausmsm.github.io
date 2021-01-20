import streamlit as st
import warnings

warnings.filterwarnings("ignore")
st.title("Quick Emblem Calculator")

st.sidebar.header("Summary")

# Character Selection
st.header("Class Selection")
from classes.character_selection import Character_selection

char = Character_selection()
st.sidebar.subheader("Class")
st.sidebar.write(f"{char.character_class}")
