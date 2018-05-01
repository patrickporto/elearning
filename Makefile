WEB=docker-compose run --service-ports web
MANAGE=$(WEB) python ava/manage.py


run:
	docker-compose up

run-debug:
	$(WEB)

migrate:
	$(MANAGE) migrate
