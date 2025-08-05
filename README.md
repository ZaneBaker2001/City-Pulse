# CityPulse: Urban Air Quality Forecast

This project uses machine learning to forecast air pollution (PM2.5) based on weather and urban data.

## Features
- Weather + pollution data ingestion
- Geospatial feature engineering
- Time-series and regression models
- Streamlit dashboard
- Daily retraining via Airflow DAG
- GitHub Actions CI

## Setup
```bash
pip install -r requirements.txt
streamlit run src/dashboard/app.py
```

## Run Tests
```bash
pytest tests/
```