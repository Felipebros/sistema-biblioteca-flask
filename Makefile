build-dev:
	docker-compose build

build:
	docker-compose build --build-arg APP_ENV=PRD

bash:
	docker-compose run app bash

list:
	docker-compose ps

tests:
	docker-compose run app py.test

up:
	docker-compose up

down:
	docker-compose down -v

clean:
	docker-compose down --volumes --rmi all
