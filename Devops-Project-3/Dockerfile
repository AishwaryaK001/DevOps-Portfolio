# Use official Python image (small)
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the app code
COPY app.py .

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Document the port the app listens on
EXPOSE 5000

# Default command to run the app
CMD ["python", "app.py"]