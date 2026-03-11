.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  setup   - build test docker image"
	@echo "  lint    - run ruff"
	@echo "  test    - run pytest"
	@echo "  scan    - run security scan placeholder"
	@echo "  run     - run uvicorn"
	@echo "  build   - build docker image"

setup:
	-docker rmi -f orders-api:test
	docker build --target test -t orders-api:test .

lint: setup
	docker run --rm orders-api:test uvx ruff format --check .
	docker run --rm orders-api:test uvx ruff check .

test: setup
	docker run --rm orders-api:test uv run -m pytest

scan:
	@echo "No security scanner configured yet for order-service"

run:
	uvicorn src.main:app --reload

build:
	docker build -t orders-api:ci-local .
