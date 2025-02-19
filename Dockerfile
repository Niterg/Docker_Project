# Use the official Python image from the Docker Hub
FROM python:3.12:version_1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY doc_app/requirements.txt .  
# Copy requirements.txt to /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY doc_app/ .  
# Copy everything from doc_app to /app

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]