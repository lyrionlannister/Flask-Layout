FROM ubuntu:22.04
WORKDIR /app
COPY . /app
RUN apt update && apt upgrade && apt install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    libpq-dev \
    gcc \
    python3-dev \
    gzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir pyarmor && .venv/bin/python3 -B compilate.py
RUN .venv/bin/pip install --no-cache-dir -r ./requirements.txt
CMD ["/bin/bash", "-c", ".venv/bin/python3 -B dist/main.py"]
