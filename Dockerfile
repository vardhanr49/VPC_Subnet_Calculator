FROM python:3.9-slim

WORKDIR /app

# Copy backend files
COPY app /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port used by Flask
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
