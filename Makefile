DOCKER_COMPOSE_FILE?=docker-compose.yaml

COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE)
APPDOCKER=$(COMPOSE) run --rm app
DAKOBED_TAG=latest


all: build web

build:
	$(COMPOSE) build

shell: services
	docker-compose run --rm app /bin/bash

web: services
	$(COMPOSE) up api

# web: services
# 	$(COMPOSE) up api ui


migrate:
	$(APPDOCKER) bard db upgrade
	$(APPDOCKER) bard db  migrate

services:
	$(COMPOSE) up -d --remove-orphans \
		$(SERVICES_CONTAINERS)

test:
	$(APPDOCKER) contrib/test.sh