# Use the official Python image as the base image
FROM python:3.10

# Install required system dependencies for OpenCV
RUN apt-get update \
    && apt-get install -y \
        libgl1 \
        libsm6 \
        libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose port 8000 for the application
EXPOSE 9000

# Command to start the FastAPI application using Uvicorn
CMD ["uvicorn", "camera_snap:app", "--host", "0.0.0.0", "--port", "9000"]
