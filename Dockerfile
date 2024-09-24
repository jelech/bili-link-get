FROM python:3.10-slim
WORKDIR /app
RUN pip install fastapi uvicorn yt-dlp python-multipart
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
