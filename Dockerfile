FROM python:3.12-slim

# Install Flask
RUN pip install flask

# Set the working directory
WORKDIR /webapp

# Copy the application code
COPY main.py /webapp/main.py

# Use the correct syntax for CMD
CMD ["python", "/webapp/main.py"]
