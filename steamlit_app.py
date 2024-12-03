import streamlit as st
import pandas as pd
import numpy as np
import random

# Function to generate random weather data
def generate_weather_data(num_days):
    dates = pd.date_range(start=pd.Timestamp.today(), periods=num_days)
    temperatures = np.random.randint(low=-10, high=35, size=num_days)  # Random temperatures between -10 and 35
    humidities = np.random.randint(low=20, high=100, size=num_days)  # Random humidity between 20% and 100%
    conditions = random.choices(['Sunny', 'Cloudy', 'Rainy', 'Stormy', 'Snowy'], k=num_days)

    weather_data = pd.DataFrame({
        'Date': dates,
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidities,
        'Condition': conditions
    })

    return weather_data

# Streamlit app
st.title("Weather Data Simulator")

# User input for number of days
num_days = st.number_input("Select number of days to simulate:", min_value=1, max_value=30, value=7)

# Generate weather data
if st.button("Generate Weather Data"):
    weather_data = generate_weather_data(num_days)
    st.write(weather_data)

    # Optionally, display a line chart of temperature and humidity
    st.line_chart(weather_data.set_index('Date')[['Temperature (°C)', 'Humidity (%)']])
