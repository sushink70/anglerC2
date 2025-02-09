# AI-C2-Detection

## Overview
AI-C2-Detection is an open-source **Django-based Command & Control (C2) server** with **AI-driven anomaly detection** to identify malicious traffic patterns. This project helps security professionals understand and mitigate threats posed by C2 frameworks.

## Features
✅ **Django-based C2 Server** – Manage agents, send commands, and retrieve responses.  
✅ **Metasploit & Empire Integration** – Control post-exploitation agents remotely.  
✅ **AI-Based Anomaly Detection** – Uses machine learning to detect suspicious network traffic.  
✅ **REST API for Automation** – Expose C2 functionality via API.  
✅ **Open Source & Extensible** – Designed for cybersecurity research and defensive analysis.  

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/AI-C2-Detection.git
cd AI-C2-Detection
```
### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3. Run the Django Server**
```bash
python manage.py migrate
python manage.py runserver
```
### **4. Train the Anomaly Detection Model**
```bash
python train_model.py
```
### **5. Test the API**
```bash
curl -X POST http://127.0.0.1:8000/api/detect_anomalies/ \
     -H "Content-Type: application/json" \
     -d '{"tcp.len": 120, "tcp.flags": 2}'
```

## Contribution
Want to contribute? Fork the repo, make improvements, and submit a pull request!

## License
This project is licensed under the **MIT License**. Use responsibly for security research and defensive purposes only.

