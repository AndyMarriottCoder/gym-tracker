FROM python:3.12-slim
WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN mkdir -p data
EXPOSE 5000
CMD ["python", "app.py"]