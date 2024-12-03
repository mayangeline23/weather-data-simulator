import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS to change background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #ADD8E6;  # Light blue background color
    }

    .sidebar .sidebar-content {
        background-color: #f5f5f5;  # Light gray background for sidebar
    }

    body {
        font-family: 'Arial', sans-serif;  # Change font to Arial
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Weather Data Simulator")

# Subheader for description
st.write("""
This app simulates weather data and visualizes the distribution of various attributes such as
temperature, humidity, wind speed, etc. You can also generate synthetic weather data and
explore it with histograms and scatter plots.
""")

# Simulate some synthetic weather data
np.random.seed(42)
n = 1000  # Number of data points
temperature = np.random.normal(loc=25, scale=5, size=n)  # Temperature in Celsius
humidity = np.random.normal(loc=60, scale=15, size=n)  # Humidity percentage
wind_speed = np.random.normal(loc=15, scale=3, size=n)  # Wind speed in km/h

# Create a DataFrame
weather_df = pd.DataFrame({
    'Temperature (°C)': temperature,
    'Humidity (%)': humidity,
    'Wind Speed (km/h)': wind_speed
})

# Display first few rows of the dataset
st.write("### Synthetic Weather Data")
st.dataframe(weather_df.head())

# Option to download the data as CSV
csv = weather_df.to_csv(index=False)
st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name="synthetic_weather_data.csv",
    mime="text/csv"
)

# Display a histogram of Temperature distribution
st.write("### Temperature Distribution")
fig, ax = plt.subplots()
sns.histplot(weather_df['Temperature (°C)'], kde=True, ax=ax, color='blue')
ax.set_title("Temperature Distribution")
st.pyplot(fig)

# Display a histogram of Humidity distribution
st.write("### Humidity Distribution")
fig, ax = plt.subplots()
sns.histplot(weather_df['Humidity (%)'], kde=True, ax=ax, color='green')
ax.set_title("Humidity Distribution")
st.pyplot(fig)

# Display a scatter plot for Wind Speed vs Temperature
st.write("### Wind Speed vs Temperature")
fig, ax = plt.subplots()
sns.scatterplot(data=weather_df, x='Temperature (°C)', y='Wind Speed (km/h)', ax=ax)
ax.set_title("Wind Speed vs Temperature")
st.pyplot(fig)

# Display a correlation heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(weather_df.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation Matrix")
st.pyplot(fig)

# Additional simulation or data manipulation options can be added here
