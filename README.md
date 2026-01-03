# 🛡️ AI-Based Cybersecurity Attack Detection System

An AI-powered cybersecurity system that analyzes network traffic patterns and classifies them as **Normal** or **Attack** using Machine Learning techniques.

This project demonstrates the practical use of **Artificial Intelligence in Cybersecurity**, focusing on intrusion detection using a trained ML model with a web-based interface.

---

## 📌 Project Overview

Traditional rule-based security systems struggle to detect new and evolving cyber attacks.  
This project uses **Machine Learning** to learn patterns from historical network traffic data and intelligently classify new traffic without relying on fixed rules.

The system is implemented using **Python (Flask)**, **Scikit-learn**, and **MongoDB Atlas**, and includes a dashboard for monitoring prediction history.

---

## 🎯 Key Features

- 🤖 AI-based traffic classification (Normal / Attack)
- 📊 Machine Learning model trained on NSL-KDD dataset
- 🌐 Web interface for real-time prediction
- 🗄️ MongoDB Atlas for storing prediction history
- 📈 Dashboard to view recent traffic classifications
- 🚨 Alert indication for attack-like traffic
- 🔐 Secure credential handling using environment variables
- 📱 Accessible on mobile devices

---

## 🧠 Role of Artificial Intelligence

- Learns patterns from labeled network traffic data  
- Uses **Random Forest Classifier** for supervised learning  
- Replaces static rule-based detection with intelligent decision-making  
- Generalizes to unseen traffic patterns  
- Automatically classifies traffic as **Normal** or **Attack**

---

## 🏗️ System Architecture
- User (Web Interface)
- ↓
- Flask Backend (Python)
- ↓
- Machine Learning Model (Random Forest)
- ↓
- MongoDB Atlas (Prediction Logs)


---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Programming Language | Python |
| Backend Framework | Flask |
| Machine Learning | Scikit-learn (Random Forest) |
| Dataset | NSL-KDD |
| Database | MongoDB Atlas |
| Frontend | HTML, CSS |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

- AI_Cybersecurity_System/
- │
- ├── app.py
- ├── db/
- │   └── mongo.py
- ├── ml/
- │   └── train_model.py
- ├── templates/
- │   ├── index.html
- │   └── dashboard.html
- ├── static/
- │   └── style.css
- ├── .env
- ├── .gitignore
- ├── requirements.txt
- └── README.md
