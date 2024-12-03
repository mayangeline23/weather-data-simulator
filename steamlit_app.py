import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("🌦️ Weather Data Simulator")
st.subheader("This app simulates weather conditions based on user inputs!")

# Input features
st.sidebar.header("Input Parameters")

season = st.sidebar.selectbox(
    "Select Season",
    ["Winter", "Spring", "Summer", "Autumn"]
)

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=-30,
    max_value=50,
    value=20
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=0,
    max_value=100,
    value=50
)

wind_speed = st.sidebar.slider(
    "Wind Speed (km/h)",
    min_value=0,
    max_value=150,
    value=10
)

precipitation = st.sidebar.slider(
    "Precipitation (mm)",
    min_value=0.0,
    max_value=500.0,
    value=10.0
)

# Simulated output
st.header("Simulated Weather Data")
data = {
    "Season": season,
    "Temperature (°C)": temperature,
    "Humidity (%)": humidity,
    "Wind Speed (km/h)": wind_speed,
    "Precipitation (mm)": precipitation,
    "Sky Condition": np.random.choice(["Clear", "Cloudy", "Rainy", "Stormy"], p=[0.3, 0.4, 0.2, 0.1])
}
weather_df = pd.DataFrame([data])

st.table(weather_df)

# Add data visualization
st.subheader("Weather Distribution")
chart_data = pd.DataFrame(
    np.random.randn(100, 4) * [temperature, humidity/100, wind_speed/10, precipitation/10],
    columns=["Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Precipitation (mm)"]
)
st.line_chart(chart_data)
