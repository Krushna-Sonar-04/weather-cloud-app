from flask import Flask, render_template, request, send_file
import requests
import os
from cryptography.fernet import Fernet
from datetime import datetime

app = Flask(__name__)

# ✅ Create storage folder if not exists
os.makedirs("storage", exist_ok=True)

# 🔐 FIXED ENCRYPTION KEY (PASTE YOUR GENERATED KEY HERE)
key = b'VJRBbmg-x99IckyLzPxvxP5lhB7EcSaojJVT_2IY7sE='
cipher = Fernet(key)

# 🌐 OPENWEATHER API KEY

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    return "API key not configured properly!"

# 🏠 Home page
@app.route('/')
def home():
    return render_template('index.html', weather="")

# 🌦 Get weather
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5).json()
    except:
        return render_template('index.html', weather="API Error!")

    # ✅ Reliable check
    if response.get("cod") == 200:
        temp = response['main']['temp']
        weather_desc = response['weather'][0]['description']

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        data = f"City: {city}, Temp: {temp}°C, Weather: {weather_desc}, Time: {current_time}"

        # 🔐 Encrypt data
        encrypted_data = cipher.encrypt(data.encode())

        # ✂ Split into 2 parts
        mid = len(encrypted_data) // 2
        part1 = encrypted_data[:mid]
        part2 = encrypted_data[mid:]

        # 💾 Save parts
        with open("storage/part1.bin", "wb") as f:
            f.write(part1)

        with open("storage/part2.bin", "wb") as f:
            f.write(part2)

        return render_template('index.html', weather=data)

    else:
        return render_template('index.html', weather="City not found!")

# 📥 Download + Merge + Decrypt
@app.route('/download')
def download():
    try:
        with open("storage/part1.bin", "rb") as f:
            part1 = f.read()

        with open("storage/part2.bin", "rb") as f:
            part2 = f.read()

        # 🔗 Merge
        encrypted_data = part1 + part2

        # 🔓 Decrypt
        decrypted_data = cipher.decrypt(encrypted_data)

        # 💾 Save final file
        with open("storage/final.txt", "wb") as f:
            f.write(decrypted_data)

        return send_file("storage/final.txt", as_attachment=True)

    except:
        return "⚠️ No file found. First fetch weather!"

# ▶️ Run app
if __name__ == "__main__":
    app.run
