import streamlit as st
import numpy as np
import joblib
from PIL import Image
import matplotlib.pyplot as plt

image=Image.open('weather_image.jpg')
st.image(image,caption="Weather Forecast",use_container_width=True)
model=joblib.load('weather_model.pkl')

st.title("🌦️ Weather Prediction App")
st.write("Enter weather details to predict rain:")

temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0)
pressure = st.slider("Pressure (hPa)", 950.0, 1050.0, 1013.0)
wind_speed = st.slider("Wind Speed (km/h)", 0.0, 100.0, 10.0)

if st.button("Predict Rain"):
    features = np.array([[temperature, humidity, pressure, wind_speed]])
    prediction = model.predict(features)

    # Feature Importance Plot
    importances = model.feature_importances_
    feature_names = ['Temperature', 'Humidity', 'Pressure', 'Wind Speed']

    fig, ax = plt.subplots()
    ax.barh(feature_names, importances, color='blue')
    ax.set_xlabel("Importance")
    ax.set_title("Feature Importances")
    st.pyplot(fig)

    # Prediction result
    if prediction[0] == 1:
        st.success("🌧️ It is likely to rain. Take an umbrella!")
    else:
        st.success("🌤️ No rain expected. Have a nice day!")