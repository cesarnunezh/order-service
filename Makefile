.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  setup   - install dependencies"
	@echo "  lint    - run ruff"
	@echo "  test    - run pytest"
	@echo "  scan    - run security scan placeholder"
	@echo "  run     - run uvicorn"
	@echo "  build   - build docker image"

setup:
	docker build --target test -t orders-api:test .

lint:
	docker run --rm orders-api:test ruff format --check .
	docker run --rm orders-api:test ruff check .

test:
	docker run --rm orders-api:test pytest

scan:
	@echo "No security scanner configured yet for order-service"

run:
	uvicorn src.main:app --reload

build:
	docker build -t orders-api:ci-local .
