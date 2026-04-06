FROM python:3.13.4-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD ["flask","run","--port=5000","--host=0.0.0.0"]