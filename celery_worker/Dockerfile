# Use a slim Python image as the base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=dev
ENV IS_DOCKER=True
ENV REDIS_URL=redis://localhost:6379/0
ENV DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/template_backend
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/celery_worker/

# Command to start the Celery worker
CMD ["celery", "-A", "celery_worker.tasks", "worker", "--loglevel=info"]

# docker build -t celery:latest .
# docker run -d --name celery --network=host celery
# docker build -t celery:latest . && docker run -d --name celery --network=host celery
