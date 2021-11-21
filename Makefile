build-dev:
	docker-compose build --build-arg APP_ENV=development --build-arg APP_DEBUG=True

build:
	docker-compose build --build-arg APP_ENV=production --build-arg APP_DEBUG=False

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
