# cars-api
Python Flask API

To run the app, go to the cars-api directory after cloning the project.

To run the app locally - python cars-app.py. Then navigate to 127.0.0.1:5000 in your browser. <- This port can be changed in the cars app file, I used 6446 for testing before intalling docker.

To run using docker, from the cars-api directory run the commands:
1) docker build -t cars-app:latest .
2) docker run -p 5000:5000 cars-app:latest

Then access 127.0.0.1:5000/

Once the app is running. We can see all cars, cards by ID and average price of cars by make, model or year.
All cars - 127.0.0.1:5000/cars/
Cars by ID - 127.0.0.1:5000/cars/2
Make/Model/Year Average -  127.0.0.1:5000/cars/average/Nissan OR 127.0.0.1:5000/cars/average/2002 OR 127.0.0.1:5000/cars/average/Fiesta
