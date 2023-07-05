# EnergyMap
EnergyMap is a Django-based web application that provides energy-related information. It utilizes Docker to containerize the application and PostgreSQL as the backend database.

# Development Setup
To set up and run the project locally, follow these steps:


## Prerequisites
Make sure you have Docker and Docker Compose installed on your machine.

## Clone the Repository

```
git clone https://github.com/BoukeLubach/energymap.git
cd energymap
```

## Configuration
1. Create a .env.dev file in the project root directory and define the necessary environment variables. You can use the .env.dev file as a template.

2. Update the DATABASES configuration in the settings.py file with the PostgreSQL database settings provided in the .env.dev.db file.

## Build and Run the Docker Containers

### development build
Use the following command to build and run the Docker containers for development:

```
docker-compose up -d --build
```

The EnergyMap application will be accessible at http://localhost:8040/.

```
docker-compose exec energymap python manage.py migrate
```

## Populate database
To populate the database with initial data, you can run the generate_data.py script inside the Docker container:

### Generate random new data
```
docker-compose exec energymap python generate_data.py
```

### Load data from fixture
Alternatively you can load data previously generated from the accompanied fixture
```
docker-compose exec energymap manage.py loaddata testdata.json
```

This will fill the database with the some test information.



## Documentation
EnergyMap utilizes the Django REST Framework for API documentation. You can access the documentation at http://localhost:8040/swagger/ or http://localhost:8040/redoc/.

## Testing
To run the tests for the EnergyMap project, use the following command:

```
docker-compose -f docker-compose.yml exec energymap python manage.py test
```

To generate a coverage report, run:
```
docker-compose -f docker-compose.yml exec energymap coverage run manage.py test
```

You can then view the coverage report by running:
```
docker-compose -f docker-compose.yml exec energymap coverage report
```

or 

```
docker-compose -f docker-compose.yml exec energymap coverage html
```