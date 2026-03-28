FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install requests
CMD ["python3", "filter_csv.py"]