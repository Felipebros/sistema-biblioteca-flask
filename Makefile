build-dev:
	docker-compose build --build-arg APP_ENV=development --build-arg APP_DEBUG=True

build:
	docker-compose build --build-arg APP_ENV=production --build-arg APP_DEBUG=False

bash:
	docker-compose run app bash

flask-run:
	flask run --host=0.0.0.0

flask-kill:
	kill -9 $(ps -A | grep python | awk '{print $1}')

ip-postgres:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' sistema-biblioteca-flask_db_1

list:
	docker-compose ps

tests:
	docker-compose run app py.test

up:
	docker-compose up

down:
	docker-compose down

clean:
	docker-compose down --volumes --rmi all
