server:
	python3 manage.py runserver

s:
	make server

migrate: # can also be used to create a new sqlite database
	python3 manage.py migrate

inspectdb:
	python3 manage.py inspectdb

migrations:
	python3 manage.py makemigrations

showmigrations:
	python3 manage.py showmigrations

console:
	python3 manage.py shell_plus

c:
	make console

requirements:
	pip3 install -r requirements.txt

bundle:
	make requirements

checkmigrations:
	python3 manage.py makemigrations --check --no-input --dry-run

create_admin_user:
	python3 manage.py createsuperuser

.PHONY: fetch-feeds run-celery run-celery-beat

fetch_feeds:
	python3 manage.py fetch_feeds

test:
	python3 manage.py test

statics:
	python3 manage.py collectstatic --noinput