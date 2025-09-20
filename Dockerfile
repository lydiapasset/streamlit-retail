FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install -e .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
