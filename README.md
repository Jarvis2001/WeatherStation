# 🌦️ Weather Station ML Project

An end-to-end, production-grade machine learning system to **collect**, **preprocess**, **analyse**, and **predict** local weather conditions using data from IoT sensors (ESP32, Arduino) and cloud images captured from a fixed camera setup. Designed for long-term deployment with CI/CD, data pipelines, and distributed computing in later phases.

---

## 🚀 Project Goals

- Build a **mini weather station** at your window
- Continuously collect sensor and cloud image data
- Preprocess and store data using a **secure, structured pipeline**
- Train a machine learning model (from scratch) on this multimodal dataset
- Deploy a **local MLOps system** for automated updates and predictions
- Support both **live sensors** and **cloud-based synthetic data** sources

---

## 📐 System Architecture

               +------------------------+
               |   Weather APIs (fallback) |
               +------------------------+
                         |
                         v
      +--------------------+ Wi-Fi +------------------+
       | ESP32 / Arduino | --------> | PC/Server Node |
       | (Sensors + Camera)| | Python Services |
      +--------------------+ +------------------------+
                         |
                         v
                +-------------------+ |
                 | Data Ingestion |
                 | Data Cleaning |
                 | Validation (Pydantic) |
                 | Logging (hourly) |
                +-------------------+
                        |
                        v
              +-------------------+
               | MongoDB (NoSQL) |
               | Raw & Cleaned |
               | Sensor & Images |
              +-------------------+
                        |
                        v
              +-------------------+
              | Model Training |
              | Predictions |
              +-------------------+
                       |
                       v
              +-------------------+
              | MLOps Pipelines |
              | Reports (PDF/XLSX) |
              | Dockerized System |
              +-------------------+


---

## 📦 Features (Phase 1)

- ✅ Secure hourly data ingestion pipeline (micro-batching)
- ✅ Sensor cleaning and normalization (C → K, m/s → km/h, etc.)
- ✅ Schema validation using **Pydantic**
- ✅ MongoDB-based NoSQL storage for sensor + cloud image metadata
- ✅ Logging system for IoT & PC-side events
- ✅ Fully functional CI pipeline (GitHub Actions)
  - Linting with `flake8`, formatting with `black`
  - Unit tests with `pytest`
- ✅ Modular and testable Python codebase

---

## 🔧 Tech Stack

| Layer                 | Tool/Tech           |
|----------------------|---------------------|
| Microcontroller      | ESP32, Arduino UNO  |
| Language             | Python 3.11         |
| Database             | MongoDB             |
| Validation           | Pydantic            |
| Testing              | pytest              |
| Linting              | flake8, black       |
| CI/CD                | GitHub Actions      |
| Image Metadata       | ESP32-CAM (JPG + JSON) |
| Optional (Future)    | Spark, Snowflake (LocalStack), Docker, Kafka |

---

## 📁 Project Structure

```
weather_station_ml/
├── src/
│ ├── ingestion/ # Sensor data collectors
│ ├── transformation/ # Cleaning and normalization
│ ├── validation/ # Pydantic schemas
│ ├── database/ # MongoDB client logic
│ ├── logging/ # Log config for IoT + PC
│ └── utils/ # Time, config, helpers
│
├── tests/ # Pytest-based unit tests
├── data/ # Raw and processed samples
├── notebooks/ # Jupyter for EDA/modeling
├── configs/ # App settings, secrets, etc.
├── .github/workflows/ # GitHub Actions CI files
├── Dockerfile # (Optional) Container build
├── requirements.txt
└── README.md
```

---

## 🧪 Testing & CI

Run locally:
```
pytest tests/
```

-CI/CD is powered by GitHub Actions, and automatically:

-Lints with flake8

-Checks formatting with black

## Clone + Install
```console
-git clone https://github.com/Jarvis2001/weather_station_ml.git
-cd weather_station_ml
-python -m venv venv
-source venv/bin/activate  # or .\venv\Scripts\activate on Windows
-pip install -r requirements.txt
```

## Start MongoDB (if local)
```docker
docker run -d -p 27017:27017 --name weather_mongo mongo:6.0
```
##Future Roadmap (Phases 2+)
 - Secure camera image streaming and lossless compression

 - Daily weather report generation (PDF/Excel)

 - Cloud-based backups and training

 - Distributed compute clusters (LLMs, cluster schedulers)

 - Full MLOps support (Docker, CI/CD for model updates)

 - Vision AI annotation of cloud images

 - Human-like interface using LLMs for querying the station

 - Runs tests on all pushes to main
