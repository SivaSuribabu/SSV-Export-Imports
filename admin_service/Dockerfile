FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask mysql-connector-python
EXPOSE 5004
CMD ["python", "app.py"]

