# Start from the official Python image.
FROM python:3.12-slim AS base

# Set the working directory in the container.
WORKDIR /app

# Install system dependencies.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies.
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose port 5000.
EXPOSE 5000

# Set environment variables.
ENV PYTHONUNBUFFERED=1
# Dev variables below to be overwritten on deployment to stage and prod
ENV ENVIRONMENT=dev
ENV IS_DOCKER=True
ENV DATABASE_URL=postgresql://postgres:postgres@localhost:5432/template_backend
ENV TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/template_backend__tests
ENV SECRET_KEY=HDGj3giTASYDTvkwekHQG67hiADUguyugjDAGSD6gk6jGAJ3SD2GUQI4weK5AJShGASDOnEFwLHxEYbhoUHAODIUGuy
ENV AUTH_SECRET_KEY=ljqELK-ODjoai3UAHSDKugKAJSgja2HDADgkJLFjGALJSHDG76GHAKSDKjf5AH5kjhAKDJu65765DASKhkASDh
ENV ALLOWED_ORIGINS="*"
ENV REDIS_URL=redis://localhost:6379/0
ENV GOOGLE_OAUTH_CLIENT_ID=your-client-id-from-google-cloud-console
ENV GOOGLE_OAUTH_CLIENT_SECRET=your-client-secret-from-google-cloud-console


# Run the application using Uvicorn.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

## Commands for use locally
# docker build -t backend-template:latest .
# docker run -p 5000:5000 backend-template:latest

# docker build -t backend-template:latest . && docker run -p 5000:5000 backend-template:latest
