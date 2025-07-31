🌦️ Weather Prediction App
This is a simple and interactive Weather Prediction App built using Streamlit and scikit-learn. The app predicts whether it will rain or not based on weather parameters like temperature, humidity, pressure, and wind speed.



🔍 Features
Predicts the likelihood of rain based on user inputs.

Uses a trained Random Forest model (weather_model.pkl).

Displays feature importance in a horizontal bar chart.

Clean and user-friendly interface.

Built with Streamlit, NumPy, Pillow, and Matplotlib.

📦 Requirements
Install the required libraries using:

bash
Copy
Edit
pip install -r requirements.txt
🔧 Project Structure
bash
Copy
Edit
weather-prediction-app/
│
├── weather_app.py                 # Streamlit app code
├── weather_model.pkl      # Trained ML model
├── weather_image.jpg      # Display image in the app
├── requirements.txt       # Python dependencies
└── README.md              # This file
🚀 How to Run
bash
Copy
Edit
streamlit run app.py
Make sure the files weather_model.pkl and weather_image.jpg are in the same directory as app.py.

🧠 Model Details
The model is trained using Random Forest Classifier with weather-related features. It outputs binary classification: Rain or No Rain.

📊 Feature Inputs
Temperature (°C)

Humidity (%)

Pressure (hPa)

Wind Speed (km/h)