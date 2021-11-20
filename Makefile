build:
	docker-compose build

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
