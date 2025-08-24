# Simple Smart Home Simulation
import random  # For fake IoT data

def simulate_iot_sensor():
    return random.randint(20, 30)  # Fake temperature

temp = simulate_iot_sensor()
if temp > 25:
    print("It's hot! Turning on fan.")  # Simple "ML" decision (we'll add real ML later)
else:
    print("Comfortable. No action.")