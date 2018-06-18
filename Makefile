export ENV=env
export FLASK_APP=zamboni/api/server.py

run:
	- flask run

dev:
	- export FLASK_DEBUG=1 && flask run

test:
	- pytest --flake8 ||: