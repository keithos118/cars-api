# cars-api
Python Flask API. 
This API uses Python, Flask, SQLAlchemy, Flask Swagger UI. The response is returned in JSON format.
There is additional screenshots added in 

To run the app, go to the cars-api directory after cloning the project.

To run the app locally - python cars-app.py. Then navigate to 127.0.0.1:5000 in your browser. <- This port can be changed in the cars app file, I used 6446 for testing before intalling docker.

To run using docker, from the cars-api directory run the command:
1) docker run -p 5000:5000 cars-app:latest

Then access 127.0.0.1:5000/

Once the app is running. We can see all cars, cards by ID and average price of cars by make, model or year.
1) All cars - 127.0.0.1:5000/cars/
2) Cars by ID - 127.0.0.1:5000/cars/2
3) Make/Model/Year Average -  127.0.0.1:5000/cars/average/Nissan OR 127.0.0.1:5000/cars/average/2002 OR 127.0.0.1:5000/cars/average/Fiesta
4) Average of Make, model and year - http://127.0.0.1:5000/cars/average/Ford/Fiesta/2002

To view the documentation, we can access the swagger docs
1) http://127.0.0.1:5000/api/docs/

This will display and test the functionality.
