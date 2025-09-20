# Retail Sales Streamlit Project

[![CI](https://github.com/lydia/streamlit-retail/actions/workflows/ci.yml/badge.svg)](https://github.com/lydia/streamlit-retail/actions/workflows/ci.yml)

This project is an **application** built with **Streamlit** for exploring retail sales data.  
It includes **Docker containerization**, **unit tests**, and a **CI workflow via GitHub Actions**.

---

## Features

- Load and filter the synthetic retail sales dataset (~1000 rows)
- Explore sales time series by store
- Train a simple regression model (LinearRegression) to predict sales from month and promo flag
- Unit tests for data loading and filtering
- Dockerfile to containerize the app
- GitHub Actions workflow to automatically run tests

---

## Project Structure

```
streamlit_retail_project/
├─ app.py                  # Streamlit entrypoint
├─ data/retail_sales.csv   # Dataset
├─ src/
│  ├─ __init__.py
│  ├─ data.py
│  └─ model.py
├─ tests/
│  └─ test_data.py
├─ requirements.txt
├─ Dockerfile
├─ setup.py
└─ .github/workflows/ci.yml
```

---

## Links

- **GitHub repository** : [https://github.com/lydia/streamlit-retail](https://github.com/lydia/streamlit-retail)  
- **DockerHub image** : [https://hub.docker.com/r/lydiapasset/retail-app](https://hub.docker.com/r/lydiapasset/retail-app)

---

## Quick Start (local)

```bash
# Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install project and dependencies
pip install -e .
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## Run Tests

```bash
pytest -q
```

All tests are included to verify data loading and filtering functions.

---

## Docker Build & Run

```bash
# Build Docker image
docker build -t lydiapasset/retail-app .

# Run the container
docker run -p 8501:8501 lydiapasset/retail-app
```

Then open your browser at `http://localhost:8501` to access the app.

---

## Model Results

- MAE (Mean Absolute Error) on the test set: **≈ 6.61**
- The model predicts daily store sales based on the month and a promotion flag.

---

## CI / GitHub Actions

- All commits automatically trigger tests via GitHub Actions
- CI badge is displayed at the top of this README
