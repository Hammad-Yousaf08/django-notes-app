FROM python:3.10-slim

# Working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Docker if necessary (without sudo)
RUN apt-get update && apt-get install -y docker.io

# Copy source code
COPY . .

# Run database migrations (if necessary)
RUN python manage.py migrate

# Expose port (adjust if needed)
EXPOSE 8000

# Run the application (FastAPI example, can be changed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
