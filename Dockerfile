FROM python:3.9

#working directory
WORKDIR /app

#installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copying app code
COPY . .

#Flask port
EXPOSE 8000

#starting with Gunicorn
CMD ["gunicorn", "app:app", "--workers=4", "--bind=0.0.0.0:8000"]




