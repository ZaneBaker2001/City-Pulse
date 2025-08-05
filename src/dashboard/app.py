import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import folium_static

st.title("CityPulse: Urban Air Quality Forecast")

model = joblib.load("model.pkl")

st.sidebar.header("Input Features")
temp = st.sidebar.slider("Temperature (°C)", -10, 40, 20)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.sidebar.slider("Wind Speed (m/s)", 0, 20, 3)
hour = st.sidebar.slider("Hour", 0, 23, 12)
dayofweek = st.sidebar.slider("Day of Week (0=Mon)", 0, 6, 2)
pm25_rolling = st.sidebar.slider("Rolling PM2.5", 0, 300, 75)

input_df = pd.DataFrame({
    "temp": [temp],
    "humidity": [humidity],
    "wind_speed": [wind_speed],
    "hour": [hour],
    "dayofweek": [dayofweek],
    "pm25_rolling": [pm25_rolling]
})

prediction = model.predict(input_df)[0]
st.subheader("Predicted PM2.5 Level")
st.metric("PM2.5 (µg/m³)", f"{prediction:.2f}")

st.subheader("Map of Monitoring Stations")
m = folium.Map(location=[51.5, -0.12], zoom_start=10)
folium.Marker([51.5, -0.12], popup="Sample Station", tooltip="Station A").add_to(m)
folium_static(m)