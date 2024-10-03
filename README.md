# Teams Management Django Project

This is a Django project for managing teams and team members. The project includes APIs for performing CRUD operations on teams and users.

## Installation
Follow these steps to set up the project locally:

Clone the repository and switch to the project directory:
```shell
git clone https://github.com/AntonKorinchuk/Teams-management.git
cd Teams-management
```

Create a virtual environment:
```shell
python -m venv venv
```

Activate the virtual environment:
On Windows:
```shell
 venv\Scripts\activate
 ```
On macOS and Linux:
```shell
source venv/bin/activate
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Apply migrations:
```shell
python manage.py migrate
```

### Rename .env.template to .env file and populate it with the required data


Run:
```shell
python manage.py runserver
```
# Run with Docker
Docker should be installed

Build the Docker image
```shell
docker build -t teams-management .
```

Run the Docker container:
```shell
docker run -p 8000:8000 teams-management
```

### Use http://127.0.0.1:8000/ or http://localhost:8000/ 

# API Overview
## Team Endpoints

- GET /api/manager/v1/teams/
Retrieve a list of all teams and their associated persons.

- POST /api/manager/v1/teams/
Create a new team with a list of persons.

- GET /api/manager/v1/teams/{id}/
Retrieve details of a specific team by its ID.

- PUT /api/manager/v1/teams/{id}/
Update the details of a specific team.

- DELETE /api/manager/v1/teams/{id}/
Delete a team by its ID.

## Person Endpoints
- GET /api/manager/v1/persons/
Retrieve a list of all persons.

- POST /api/manager/v1/persons/
Create a new person.

- GET /api/manager/v1/persons/{id}/
Retrieve details of a specific person by their ID.

- PUT /api/manager/v1/persons/{id}/
Update the details of a specific person.

- DELETE /api/manager/v1/persons/{id}/
Delete a person by their ID.