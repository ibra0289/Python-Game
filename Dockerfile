# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY Ibra0289_Assignment4.py ./game.py

# Command to run the Python application
CMD ["python", "game.py"]


