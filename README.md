# CityPulse: Urban Air Quality Forecast

CityPulse is a full-stack data science project that predicts PM2.5 pollution levels in urban environments using weather, traffic, and geospatial data. It features machine learning models, time-series forecasting, a web dashboard, and automated retraining.

---

##  Project Structure & Descriptions

```
air-quality-forecaster/
├── airflow/
│   └── dags/
│       └── retrain_model_dag.py           # Airflow DAG for daily model retraining
├── src/
│   ├── ingest/
│   │   └── weather_api.py                 # Fetches live weather data from OpenWeatherMap API
│   ├── clean/
│   │   └── clean_air_quality.py           # Cleans air pollution data (e.g., drops NaNs, converts time)
│   ├── features/
│   │   └── engineer.py                    # Feature engineering and geospatial enrichment
│   ├── models/
│   │   ├── train_model.py                 # Trains a regression model (Random Forest)
│   │   └── forecast_pm25.py              # Time-series forecasting using Prophet
│   └── dashboard/
│       └── app.py                         # Streamlit dashboard for prediction and map visualization
├── Dockerfile                             # Docker container config for deployment
├── requirements.txt                       # Python package dependencies
└── README.md                              # Project documentation (this file)
```

---

##  Features

-  **Live Weather Ingestion** via OpenWeatherMap API
-  **Data Cleaning**: Robust handling of nulls and invalid readings
-  **Feature Engineering**: Rolling averages, time-based features
-  **Geospatial Analysis**: Add regional context using shapefiles
-  **Modeling**: Random Forest Regressor for pollution prediction, prophet for time-series forecasting
-  **Dashboard**: Streamlit UI with maps (Folium) and user inputs
-  **Automation**: Airflow DAG for daily model retraining
-  **Deployment**: Containerized via Docker

---

##  Quickstart

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Dashboard

```bash
streamlit run src/dashboard/app.py
```

### 3. Run Airflow DAG (example)

```bash
# Navigate to Airflow folder and use Airflow CLI
airflow dags trigger retrain_model_daily
```



