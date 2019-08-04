FROM python:3.7.4
COPY . /cars-app
WORKDIR /cars-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["cars-app.py"]