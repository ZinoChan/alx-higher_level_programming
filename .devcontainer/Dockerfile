# Use an official Python runtime as a parent image
FROM python:3.8.5-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8000

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
