import streamlit as st
from main import *


def low_bmi():
    st.warning(f"Your BMI value is too low {username}!")


def normal_bmi():
    st.success(f"This value is good {username}! It means that you are fit")


def over_weight():
    st.warning(f"Watch your weight {username}")


def obesity():  # BMI result higher than 40
    st.warning(f"Oops! You need to consult your Doctor {username}")

