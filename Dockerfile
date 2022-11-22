FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client

WORKDIR /djangoapp

COPY requirements.txt /djangoapp/requirements.txt

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY env.sample /djangoapp/.env

COPY . /djangoapp

# running migrations
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py generate-api

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]

