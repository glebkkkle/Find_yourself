# ---------- Base image ----------
FROM python:3.10-slim

# ---------- Environment setup ----------
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# ---------- Working directory ----------
WORKDIR /app

# ---------- System dependencies ----------
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    pkg-config \
    libcairo2-dev \
    libgirepository1.0-dev \
    libyaml-dev \
    libcurl4-openssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy project files ----------
COPY . /app

# ---------- Python dependencies ----------
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Expose port ----------
EXPOSE 8501

# ---------- Entry point ----------
CMD ["python3", "src/ds.py"]
