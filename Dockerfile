FROM python:3.10-slim

WORKDIR /medbot

COPY g.txt .

RUN pip install --no-cache-dir -r g.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
