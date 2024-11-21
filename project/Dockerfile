# Use a Python base image from the official repository
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8080

# Set the command to run the Flask app
CMD ["python", "app.py"]
