# 🌦 Weather Cloud SaaS Application

## 📌 Project Overview
This project is a **Weather Forecasting SaaS Application** developed using Flask and deployed on cloud (Render).  
It demonstrates the concept of **Software as a Service (SaaS)** along with a **mini cloud storage system inspired by HDFS**.

---

## 🎯 Aim
To set up a cloud-based SaaS application and implement basic cloud storage operations such as:
- File segmentation (splitting into blocks)
- Encryption and secure storage
- Download and reconstruction of data

---

## 🚀 Features

### 🌦 Weather Forecast
- Fetch real-time weather data using OpenWeather API
- Displays temperature, weather condition, and time

### 🔐 Data Encryption
- Uses **Fernet encryption** to secure data

### 🧩 File Splitting (HDFS Simulation)
- Data is divided into multiple parts (`part1.bin`, `part2.bin`)
- Simulates distributed storage

### ☁️ Cloud Storage (Simulated)
- Files stored in `storage/` directory acting as cloud

### 📥 Download & Reconstruction
- Merges split files
- Decrypts data
- Provides final downloadable report

---

## 🛠 Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Flask (Python)
- **API:** OpenWeather API
- **Encryption:** Cryptography (Fernet)
- **Deployment:** Render (Cloud Platform)

---

## ⚙️ How It Works

1. User enters city name  
2. Weather data is fetched using API  
3. Data is encrypted  
4. Encrypted data is split into blocks  
5. Blocks are stored in cloud (`storage/`)  
6. On download:
   - Blocks are merged  
   - Data is decrypted  
   - Final file is generated  

---

## 📂 Project Structure
weather-cloud-app/
│
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
├── storage/
│ ├── part1.bin
│ ├── part2.bin
│ └── final.txt
└── README.md


---

## ☁️ Deployment

The application is deployed on **Render (Free Tier)**.

### ⚠️ Note:
- Free tier uses **temporary storage**
- Data may reset after inactivity

---

## 🔐 Security

- API keys are stored using **environment variables**
- Data is encrypted before storage

---

## 👨‍💻 Team Members

- Krushna Sonar  
- Om Talape  
- Spandan Thul  
- Srushti Patil  

---

## 🎤 Conclusion

This project successfully demonstrates:
- SaaS deployment on cloud  
- Secure data handling  
- File segmentation and reconstruction  
- Basic simulation of HDFS concepts  

---

## 📌 Future Improvements

- Add database for persistent storage  
- Implement user authentication  
- Real distributed storage system  
- UI enhancements with animations  

---

## ⭐ Acknowledgement

This project is developed for academic purposes to understand cloud computing concepts and SaaS architecture.
