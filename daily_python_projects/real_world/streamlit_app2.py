import streamlit as st

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

st.title("Live Distance Converter")
mode = st.selectbox("Conversion type:", ["KM to Miles", "Miles to KM"])
value = st.number_input("Enter value:", min_value=0.0)

if mode == "KM to Miles":
    st.write(f"{value} km is {km_to_miles(value):.2f} miles")
else:
    st.write(f"{value} miles is {miles_to_km(value):.2f} km")
