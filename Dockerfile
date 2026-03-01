FROM python:3.11-slim

WORKDIR /app

# Correct spelling
COPY requirements.txt /app/

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY main.py /app/

EXPOSE 8080

# Run uvicorn with 6 workers
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "6"]
