# Use the official Python image as a parent image
FROM python:3.9-alpine
LABEL authors="denisle"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define the command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]