import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# App title and header
st.title("Weather Data Simulator 🌦️")
st.subheader("Generate, Analyze, and Visualize Weather Data")

# Sidebar: User Input for Data Generation
st.sidebar.header("Weather Data Parameters")
num_days = st.sidebar.slider("Number of Days", min_value=7, max_value=365, value=30)
min_temp = st.sidebar.slider("Minimum Temperature (°C)", -30, 30, -10)
max_temp = st.sidebar.slider("Maximum Temperature (°C)", min_temp, 50, 35)
min_humidity = st.sidebar.slider("Minimum Humidity (%)", 0, 50, 10)
max_humidity = st.sidebar.slider("Maximum Humidity (%)", min_humidity, 100, 90)
min_wind_speed = st.sidebar.slider("Minimum Wind Speed (km/h)", 0, 10, 2)
max_wind_speed = st.sidebar.slider("Maximum Wind Speed (km/h)", min_wind_speed, 100, 50)
min_precipitation = st.sidebar.slider("Minimum Precipitation (mm)", 0, 10, 0)
max_precipitation = st.sidebar.slider("Maximum Precipitation (mm)", min_precipitation, 50, 20)

# Generate Weather Data
st.header("Generated Weather Data")
weather_data = {
    "Date": pd.date_range(start=pd.Timestamp.today(), periods=num_days),
    "Temperature (°C)": np.random.uniform(min_temp, max_temp, num_days).round(2),
    "Humidity (%)": np.random.uniform(min_humidity, max_humidity, num_days).round(2),
    "Wind Speed (km/h)": np.random.uniform(min_wind_speed, max_wind_speed, num_days).round(2),
    "Precipitation (mm)": np.random.uniform(min_precipitation, max_precipitation, num_days).round(2),
}
weather_df = pd.DataFrame(weather_data)
st.dataframe(weather_df)

# Download Data as CSV
st.subheader("Download Weather Data")
csv = weather_df.to_csv(index=False).encode("utf-8")
st.download_button(label="Download CSV", data=csv, file_name="weather_data.csv", mime="text/csv")

# Visualization
st.header("Weather Data Visualization")

# Select graph type
graph_type = st.selectbox("Choose Graph Type", ["Line Chart", "Bar Chart", "Histogram"])

if graph_type == "Line Chart":
    st.line_chart(weather_df[["Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Precipitation (mm)"]])
elif graph_type == "Bar Chart":
    st.bar_chart(weather_df[["Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Precipitation (mm)"]])
elif graph_type == "Histogram":
    st.subheader("Temperature Distribution")
    
    # Option 1: Altair for Histogram
    temperature_histogram = alt.Chart(weather_df).mark_bar().encode(
        alt.X("Temperature (°C)", bin=True, title="Temperature (°C)"),
        alt.Y("count()", title="Frequency")
    ).properties(width=600, height=400)
    st.altair_chart(temperature_histogram)

    # Option 2: Matplotlib for Histogram
    st.write("Matplotlib Version:")
    fig, ax = plt.subplots()
    ax.hist(weather_df["Temperature (°C)"], bins=20, color="skyblue", edgecolor="black")
    ax.set_title("Temperature Distribution")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
