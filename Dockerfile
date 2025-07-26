# Use a slim Python image compatible with amd64
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy app folder into the container
COPY app/ ./app/

# Move into the app directory
WORKDIR /app/app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main script
ENTRYPOINT ["python", "main.py"]
