############################################################
# Makefile for the Koden, a simple Docker container
# orchestrator
############################################################


# Make environment configuration
#############################################

SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help # Running make without args will run the help target
.NOTPARALLEL: # Run make serially

# Python environment
VENV = venv
ACTIVATE_VENV := . $(VENV)/bin/activate
PYTHON := $(VENV)/bin/python3

# Testing targets
#####################
.PHONY: test
test: ## Run all tests: unit, functional, and e2e
	@$(MAKE) test-unit

.PHONY: test-unit
test-unit: ## Run unit tests
	@$(ACTIVATE_VENV) && python3 -m unittest discover


# Helper targets
####################
.PHONY: help
help:
	@printf "\n%s\n\n" "usage: make <target>"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;36m%-30s\033[0m %s\n", $$1, $$2}'