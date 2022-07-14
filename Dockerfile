# Find an image from Docker website
FROM python:3
# Copy application or program files from image to the target creating a dir called app
COPY . /app
WORKDIR /app
# Start the application
CMD python3 Source/main.py