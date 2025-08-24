import pandas as pd  # For loading/handling data
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.ensemble import RandomForestClassifier  # Simple ML model
from sklearn.metrics import accuracy_score  # To check model performance
import streamlit as st  # For dashboard
import time  # For simulating real-time

# Step 1: Load Dataset (Simulate IoT sensors)
data = pd.read_csv('/Users/chand/OneDrive/Desktop/SMART-HOME-DEVOPS/data/HomeC_small.csv')  # Replace with your CSV path
# Clean data a bit (dataset has some issues, like summary row—skip it)
data = data[:-1]  # Remove last summary row if present
# Select relevant columns: Temperature, Humidity, Energy Use (for prediction)
X = data[['temperature', 'humidity']]  # 'use [kW]' is energy usage
# Create a simple target: High energy (1) if use > 0.5 kW, else Low (0)
data['high_energy'] = (data['use [kW]'] > 0.5).astype(int)

# Step 2: Train Simple ML Model
X = data[['temperature', 'humidity']]  # Features (IoT inputs)
y = data['high_energy']  # Target (predict if high energy/action needed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=10)  # Simple forest with 10 trees (keep mini)
model.fit(X_train, y_train)
# Test accuracy (for demo)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"ML Model Accuracy: {accuracy:.2f}")  # Print for console test

# Step 3: Dashboard with Streamlit
st.title("Smart Home Automation Dashboard")
st.write("Simulated IoT Readings and ML Predictions")

# Simulate real-time: Show "live" data from dataset rows
placeholder = st.empty()  # For updating display
for i in range(10):  # Loop 10 times for demo (simulate stream)
    row = data.iloc[i]  # Get a row as "current reading"
    temp = row['temperature']
    hum = row['humidity']
    
    # ML Prediction
    pred = model.predict([[temp, hum]])[0]
    action = "Turn on AC/Fan (High Energy Predicted)" if pred == 1 else "No Action Needed (Low Energy)"

    # Display
    with placeholder.container():
        st.write(f"Current Temperature: {temp} °C")
        st.write(f"Current Humidity: {hum} %")
        st.write(f"ML Prediction: {action}")
        st.bar_chart([temp, hum], width=200)  # Simple chart
    
    time.sleep(2)  # Wait 2 sec to simulate real-time

# Run this with: streamlit run app.py