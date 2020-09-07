.DEFAULT_GOAL := help

.PHONY: install
install:
	python3 -m venv .venv
	pip3 install -e .


.PHONY: install_test
install_test:
	python3 -m venv .venv
	.venv/bin/pip3 install -e ".[test]"

.PHONY: fmt
fmt: install_test
	black .

.PHONY: checks
checks: install_test
	black .
	isort .
	mypy .

.PHONY: clean
clean:
	rm -rf .venv

.PHONY: help
help:
	@echo ""
	@echo "Available targets:"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

