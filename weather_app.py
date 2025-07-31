import streamlit as st
import numpy as np
import joblib
from PIL import Image
import matplotlib.pyplot as plt
import base64


def set_bg_image(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #ffffff !important;
    }}
    .main-container {{
        background: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        margin: 20px auto;
        max-width: 750px;
    }}
    h1, h2, h3, p, label, .stSlider, .stButton {{
        color: black !important;
        font-weight: bold;
        font-size: 30px !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 🔹 Global style for text and buttons
st.markdown("""
<style>
body, .main-container, .stApp {
    font-size: 30px !important;
    color: #ffffff;
}
label, .stSlider label {
    font-size: 25px !important;
}
.stButton > button {
    background-color: #FF5E5E;
    color: white;
    font-size: 22px;
    padding: 0.75em 1.5em;
    border-radius: 10px;
    transition: all 0.3s ease-in-out;
    font-weight: bold;
}
.stButton > button:hover {
    background-color: #ff8080;
    transform: scale(1.05);
    color: black;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* Slider label and tick value styling */
.css-1cpxqw2, .css-1hynsf2, .css-qrbaxs, .css-1y4p8pa, .css-14xtw13 {
    font-size: 22px !important;
    font-weight: bold !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* Slider tick labels (min, max, default values) */
div[data-baseweb="slider"] > div > div > div > div {
    font-size: 22px !important;
    color: #ffffff !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)


# 🔹 Set background image
set_bg_image("background.jpg")

# 🔹 Load model
model = joblib.load('weather_model.pkl')

# 🔹 Start UI container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

image = Image.open('weather_image.jpg')
st.image(image, caption="Weather Forecast", use_container_width=True)

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
    fig.patch.set_alpha(0.0)  
    ax.set_facecolor("none")  
    ax.barh(feature_names, importances, color='orange')
    ax.set_xlabel("Importance", color='black')
    ax.set_title("Feature Importances", color='black')
    ax.tick_params(colors='black')
    st.pyplot(fig)

    # Prediction result
    if prediction[0] == 1:
        st.success("🌧️ It is likely to rain. Take an umbrella!")
    else:
        st.success("🌤️ No rain expected. Have a nice day!")

# 🔹 Close container
st.markdown('</div>', unsafe_allow_html=True)

