FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /medbot

# Copy requirements first and install dependencies
COPY g.txt .

RUN pip install --no-cache-dir -r g.txt

# Copy the rest of the application
COPY . .

# Expose the port (Render/Railway usually uses 8080)
EXPOSE 8080

# Run the app using gunicorn (assuming your app is in app.py and app = Flask(...))
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
