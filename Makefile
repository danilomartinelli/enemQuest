SHELL := /bin/bash

up:
	docker-compose up --build

down:
	docker-compose down

restart: down up

.PHONY: up down restart
