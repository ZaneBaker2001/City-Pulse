# Dockerfile for CityPulse: Urban Air Quality Forecast

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS dependencies for geopandas and Prophet
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    libgeos-dev \
    libproj-dev \
    proj-data \
    proj-bin \
    libgdal-dev \
    python3-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Streamlit-specific environment config (optional)
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true

# Expose the port Streamlit runs on
EXPOSE 8501

# Default command to run the Streamlit app
CMD ["streamlit", "run", "src/dashboard/app.py"]