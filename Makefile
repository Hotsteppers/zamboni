export ENV=env

run:
	- flask run

build-dev:
	- docker-compose -f docker-compose-dev.yml up -d --build

dev:
	- docker-compose -f docker-compose-dev.yml up

test:
	- pytest --flake8 ||:
