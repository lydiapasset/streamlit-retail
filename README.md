# Retail Sales Streamlit Project

This project is a **data science app** built with Streamlit for exploring retail sales data,
with containerization (Docker), testing, and CI (GitHub Actions).

## Features
- Load and filter synthetic retail sales dataset (~1000 rows)
- Explore time series of sales by store
- Train a simple regression model (LinearRegression) to predict sales from month and promo flag
- Unit tests for data loading and filtering
- Dockerfile to containerize the app
- GitHub Actions workflow to run tests

## Project structure
```
streamlit_retail_project/
├─ app.py                  # Streamlit entrypoint
├─ data/retail_sales.csv   # dataset
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

## Quick start (local)
```bash
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
pip install -e .
streamlit run app.py
```

## Run tests
```bash
pytest -q
```

## Docker build
```bash
docker build -t youruser/retail-app .
docker run -p 8501:8501 youruser/retail-app
```
