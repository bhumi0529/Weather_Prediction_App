import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv('weather.csv')
X = df[['temperature', 'humidity', 'pressure', 'wind_speed']]
y = df['rain']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'weather_model.pkl')
print("Model trained and saved as weather_model.pkl")
