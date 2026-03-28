import streamlit as st
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Visa Processing Time Predictor")

st.write("Enter the details below:")

emp_size = st.number_input("Employer Number of Employees")
emp_year = st.number_input("Employer Year Established")
pw_amount = st.number_input("Prevailing Wage (pw_amount_9089)")
wage_offer = st.number_input("Wage Offer")
month = st.number_input("Month (1-12)")
country_avg = st.number_input("Country Avg Processing")

if st.button("Predict"):
    input_data = [[emp_size, emp_year, pw_amount, wage_offer, month, country_avg]]
    result = model.predict(input_data)

    st.success(f"Estimated Processing Days: {result[0]:.2f}")
