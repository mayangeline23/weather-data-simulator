import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("🌦️ Weather Data Simulator")
st.subheader("Simulate weather data and explore visualizations!")

# Sidebar inputs
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

# Simulated weather data
st.header("Simulated Weather Data")
num_rows = st.slider("Number of Simulated Records", 10, 100, 20)

# Generate random weather data
data = {
    "Season": [season] * num_rows,
    "Temperature (°C)": np.random.normal(temperature, 5, num_rows),
    "Humidity (%)": np.random.normal(humidity, 10, num_rows),
    "Wind Speed (km/h)": np.random.normal(wind_speed, 5, num_rows),
    "Precipitation (mm)": np.random.normal(precipitation, 20, num_rows),
    "Sky Condition": np.random.choice(["Clear", "Cloudy", "Rainy", "Stormy"], size=num_rows, p=[0.3, 0.4, 0.2, 0.1])
}

weather_df = pd.DataFrame(data)

# Display the data as a table
st.write(weather_df)

# Allow users to download data as CSV
csv = weather_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📂 Download Data as CSV",
    data=csv,
    file_name="simulated_weather_data.csv",
    mime="text/csv"
)

# Add visualizations
st.header("Weather Data Visualization")

# Select graph type
graph_type = st.selectbox("Choose Graph Type", ["Line Chart", "Bar Chart", "Histogram"])

if graph_type == "Line Chart":
    st.line_chart(weather_df[["Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Precipitation (mm)"]])
elif graph_type == "Bar Chart":
    st.bar_chart(weather_df[["Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Precipitation (mm)"]])
elif graph_type == "Histogram":
    st.subheader("Temperature Distribution")
    st.hist_chart(weather_df["Temperature (°C)"])

# Summary statistics
st.header("Summary Statistics")
st.write(weather_df.describe())
