FROM python:3.10

# Set working directory inside the container
WORKDIR /medbot

# Copy requirements first and install (allows caching of deps)
COPY g.txt .

RUN pip install --no-cache-dir -r g.txt

# Copy the rest of the application
COPY . .

# Expose Flask's default port
EXPOSE 8080

# Run the Flask app
CMD ["python3", "app.py"]
