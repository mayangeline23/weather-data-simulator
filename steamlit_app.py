import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Function to generate random weather data with seasonal variations
def generate_weather_data(num_days, season):
    if season == "Winter":
        temp_range = (-10, 5)
        humidity_range = (30, 80)
    elif season == "Spring":
        temp_range = (5, 20)
        humidity_range = (40, 90)
    elif season == "Summer":
        temp_range = (15, 35)
        humidity_range = (20, 70)
    else:  # Fall
        temp_range = (0, 20)
        humidity_range = (40, 80)

    dates = pd.date_range(start=pd.Timestamp.today(), periods=num_days)
    temperatures = np.random.randint(low=temp_range[0], high=temp_range[1], size=num_days)
    humidities = np.random.randint(low=humidity_range[0], high=humidity_range[1], size=num_days)
    conditions = random.choices(['Sunny', 'Cloudy', 'Rainy', 'Stormy', 'Snowy'], k=num_days)

    weather_data = pd.DataFrame({
        'Date': dates,
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidities,
        'Condition': conditions
    })

    return weather_data

# Add custom CSS for background design
st.markdown(
    f"""
    <style>
        .stApp {{
            background: url("background.jpg");
            background-size: cover;
        }}
        h1 {{
            color: white;
            text-shadow: 2px 2px 5px black;
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 2rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("Weather Data Simulator")

# User input for number of days and season
num_days = st.number_input("Select number of days to simulate:", min_value=1, max_value=30, value=7)
season = st.selectbox("Select the season:", ["Winter", "Spring", "Summer", "Fall"])

# Generate weather data
if st.button("Generate Weather Data"):
    weather_data = generate_weather_data(num_days, season)
    st.write(weather_data)

    # Optionally, display a line chart of temperature and humidity
    st.line_chart(weather_data.set_index('Date')[['Temperature (°C)', 'Humidity (%)']])

    # Visualize the distribution of temperature and humidity
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].hist(weather_data['Temperature (°C)'], bins=10, color='blue', alpha=0.7)
    ax[0].set_title('Temperature Distribution')
    ax[0].set_xlabel('Temperature (°C)')
    ax[0].set_ylabel('Frequency')

    ax[1].hist(weather_data['Humidity (%)'], bins=10, color='green', alpha=0.7)
    ax[1].set_title('Humidity Distribution')
    ax[1].set_xlabel('Humidity (%)')
    ax[1].set_ylabel('Frequency')

    st.pyplot(fig)

    # Allow users to download the data as a CSV file
    csv = weather_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download Weather Data as CSV", csv, "weather_data.csv", "text/csv")
