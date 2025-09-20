FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Upgrade pip and install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -e .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
