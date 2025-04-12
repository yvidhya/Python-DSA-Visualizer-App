🚦 Smart TrafficSense: Real-Time Traffic Monitoring System

A full-stack web application to monitor, visualize, and analyze real-time traffic congestion data using live feeds and historical analytics.

📌 Overview
This project uses the MERN stack to deliver a scalable dashboard with congestion maps, heatmaps, and live data charts. It's designed to simulate a real-world smart city application with modern UI, real-time updates, and predictive potential.

---

⚙️ Tech Stack

Frontend
- React.js
- Chart.js
- Google Maps JavaScript API

Backend
- Node.js
- Express.js
- Socket.io (for WebSocket communication)

Database
- MongoDB (for historical data storage)

Tools & Platforms
- Visual Studio Code
- Git + GitHub
- Google Cloud Platform / Render / Vercel (for deployment)

---

✨ Features
- 📍 Real-time traffic congestion overlays on Google Maps
- 🔁 Live data updates via Socket.io
- 📊 Historical traffic trend analysis using Chart.js
- 📡 WebSocket-powered client-server communication
- 🔐 Secure architecture and modular design

---

🧑‍💻 Getting Started

Prerequisites
- Node.js and npm installed
- MongoDB running locally or MongoDB Atlas
- Google Maps API key

Installation Steps

```bash
# Clone the repo
git clone https://github.com/yourusername/Smart-TrafficSense.git
cd Smart-TrafficSense
#Backend Setup
cd server
npm install
node index.js
#Frontend setup
cd ../client
npm install
npm start
