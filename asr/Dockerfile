# Use a PyTorch base image with CUDA support removed (if not needed)
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY asr_api.py .

# Expose the API port
EXPOSE 8001

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "asr_api:app", "--host", "0.0.0.0", "--port", "8001"]

# from neleht.@Nelehs-MacBook-Air 
# docker build -t asr-api ./asr
# docker run -p 8001:8001 asr-api

# Test the API with curl
# curl -F "file=@/Users/neleht./Desktop/nosync/HTX_xData_test/common_voice/cv-valid-dev/cv-valid-dev/sample-000000.mp3" http://localhost:8001/asr



