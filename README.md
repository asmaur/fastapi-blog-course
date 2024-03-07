# API Development

![Python](https://img.shields.io/badge/Python-%233776ab.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/fastapi-%23009485.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![Mysql](https://img.shields.io/badge/mysql-%23316192.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%231d63ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

This project is an API built using **Pyhon, FastAPI, MySQL as the database, JWT for authentication control.**

This project was build for API Development with Python and FastAPI Course and may be available on my [Youtube Channel](https://www.youtube.com/@wanubit), to demonstrate how to configure Authentication and Implement Security using JWT token.

## Table of Contents

- [API Development](#api-development)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Database](#database)
  - [Contributing](#contributing)

## Installation

1. Clone the repository:

```bash
git@github.com:asmaur/fastapi-blog-course.git
```

Make sure you have Docker and Docker compose installed and working on your computer

## Usage

1. Start the application with Docker compose
   `docker compose up`

   if the app fail to connect to the database at first run. Kill all container and try again.

2. The API will be accessible at http://localhost:8080/

## API Endpoints

The API provides the following endpoints:

```markdown
GET /blog - Retrieve a list of all post. (all authenticated users)

GET /blog/{id} - Retrieve a list of all products. (all authenticated users)

POST /blog - Create a new post (all authenticated users).

PUT /blog/{id} - Update a post. (all authenticated users)

DELETE /blog/{id} - Delete a post. (all authenticated users)

POST /login - Login into the App

POST /users - Register a new user into the App
```

## Authentication

The API uses JWT for authentication control.

## Database

The project utilizes [MySQL](https://www.mysql.com/) as the database. The necessary database migrations are managed using `SQLAlchemy`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request to the repository.

When contributing to this project, please follow the existing code style, [commit conventions](https://www.conventionalcommits.org/en/v1.0.0/), and submit your changes in a separate branch.
