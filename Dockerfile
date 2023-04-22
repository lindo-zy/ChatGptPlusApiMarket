FROM tiangolo/uvicorn-gunicorn:python3.11

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3","main.py"]
