# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the app
CMD ["streamlit", "run", "app.py"]