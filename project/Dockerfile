FROM python:3.8-slim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY src /opt/ml/code
WORKDIR /opt/ml/code

ENTRYPOINT ["python3", "app.py"]
