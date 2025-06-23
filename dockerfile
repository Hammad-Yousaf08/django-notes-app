FROM python:3.10-slim
#hlw this is HY from ajk

# Working directory inside container
WORKDIR /app


# Copy dependency file
COPY requirements.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy source code
COPY . .
RUN python manage.py migrate

# Expose port (adjust if needed)
EXPOSE 8000


# Run the application (FastAPI example, can be changed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
