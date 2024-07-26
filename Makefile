SERVICE = api

build:
	docker compose build

up:
	docker compose up -d ${SERVICE}

down:
	docker compose down

test:
	docker compose up -d api_test && \
	docker compose exec -it api_test pytest -v src/tests/

lint:
	docker run --rm --volume ./:/src --workdir /src pyfound/black:latest_release black --check .

format:
	docker run --rm --volume ./:/src --workdir /src pyfound/black:latest_release black .

shell:
	docker compose up -d api_test && \
	docker compose exec -it api_test bash

logs:
	docker-compose logs -f ${SERVICE}

re: down build up
