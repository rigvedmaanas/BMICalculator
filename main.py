import streamlit as st

def calculateBMI():
    bmi = weight/(height*height)
    if bmi <= 18.5:
        st.error(f"Your BMI is {bmi}. Underweight")
    elif bmi > 18.5 and bmi <= 24.9:
        st.success(f"Your BMI is {bmi}. Normal weight")
    elif bmi > 24.9 and bmi <= 29.9:
        st.warning(f"Your BMI is {bmi}. Overweight")
    else:
        st.error(f"Your BMI is {bmi}. Obesity")

st.write("# BMI **(Body Mass Index)**")
weight = st.number_input(label="Weight **(kg)**", value=40)
height = st.number_input(label="Height **(m)**", value=1.6)
st.button(label="Check BMI", on_click=calculateBMI)