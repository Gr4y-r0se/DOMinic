# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 443 available to the world outside this container
EXPOSE 443

# Define environment variable
ENV NAME DOMinic

# Run app.py when the container launches
CMD ["python", "app.py"]

# Build and run
# docker build -t dominic .
# docker run -p 443:443 dominic
