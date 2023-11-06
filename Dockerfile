# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt
# Install any dependencies
RUN pip install --upgrade -r requirements.txt
# Copy the content of the local repo
COPY . .

# # Add the current directory contents into the container at /app
# ADD . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Make port 80 available to the world outside this container
# EXPOSE 80

# # Run app.py when the container launches
# CMD ["python", "app.py"]
