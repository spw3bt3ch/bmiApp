import streamlit as st
from functions import *

bmi_definition = f"""A BMI (Body Mass Index) calculator is a tool used 
to assess an individual's body weight in relation to their height. 
It provides an estimate of body fat and categorizes individuals into 
different weight status categories.
"""

col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    st.image("BMI2.jpg", width=300)
    st.write(bmi_definition)


with col2:
    try:
        st.title("BMI CALCULATOR")
        username = st.text_input("NAME: ", placeholder="Username")
        weight = st.number_input("WEIGHT (kg): ")
        height = st.number_input("HEIGHT (m - e.g 1.89): ")
        bmi_result = weight / (height * height)
        st.subheader(f"{bmi_result:.2f}")

        if bmi_result <= 18.5:
            low_bmi()

        elif (bmi_result > 18.5) and (bmi_result <= 24.99):
            normal_bmi()

        elif (bmi_result >= 25) and (bmi_result < 30):
            over_weight()

        else:
            obesity()

    except ZeroDivisionError:
        st.info("Enter your values")
