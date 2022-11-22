## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ # Get the code
$ git clone https://github.com/alejandro-sanchez1992/docker-django-postgresql
$ cd docker-django-postgresql
```

<br />

> **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ Create a new `.env` file using sample `env.sample`

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `ASSETS_ROOT`: used in assets management
  - default value: `/static/assets`
- `OAuth` via Github
  - `GITHUB_ID`=<GITHUB_ID_HERE>
  - `GITHUB_SECRET`=<GITHUB_SECRET_HERE> 

<br />

> Set Up Database

```bash
$ docker exec -it djangoapp bash
$ python manage.py makemigrations apps
$ python manage.py migrate
$ python manage.py generate-api     # optional
```

## ✨ Create Users

```bash
$ docker exec -it djangoapp bash
$ python manage.py createsuperuser
```

<br />


## ✨ API Generator

This module helps to generate secure APIs using DRF via a simple workflow: 

- Edit/add your model in `apps/models.py`
- Migrate the database:
  - `python manage.py makemigrations apps` # this will generate the new SQL
  - `python manage.py migrate`             # this will apply the changes
- Update Configuration:
  - `core/settings.py`, section `API_GENERATOR` 
- Generate the API code:
  - `python manage.py generate-api`        # the new code is saved in `apps/api`
- Access the API in the browser:
  - `/api/MODEL_NAME/`

The API is secured using the JWT token provided by `/login/jwt/` request (username & password should be provided).  

- GET requests are public (GET all, get Item)
- Mutating requests are protected by token generated based on the user credentials (`username`, `pass`). 

> Two POSTMAN Collections are provided in the `media` directory: 

- [Books API](./media/api-books.postman_collection) - that uses PORT **5000* for the api
- [Books API 2](./media/api-books-docker.postman_collection) - that uses PORT **5085* for the api (default port in Docker)

In case both port are unusable in your environment, feel free to edit the files before POSTMAN import.

<br />


