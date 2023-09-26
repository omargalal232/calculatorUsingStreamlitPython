import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

operation = st.radio("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

result = None

if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 == 0:
        st.error("Division by zero is not allowed")
    else:
        result = num1 / num2

if result is not None:
    st.write(f"Result: {result}")
