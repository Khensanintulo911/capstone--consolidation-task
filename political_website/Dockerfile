# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt if it exists
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy the rest of your code
COPY . .

# Expose the port your app runs on (update as needed, e.g. 5000 for Flask)
EXPOSE 5000

# Change this line if your main file is not app.py
CMD ["python", "app.py"]