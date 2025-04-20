FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install system-level packages for whisper, soundfile, etc.
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 6000

CMD ["python", "main.py"]
