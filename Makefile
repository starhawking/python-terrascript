
NOSE := nosetests --failed --verbose --no-byte-compile --logging-level=DEBUG --detailed-errors
COVERAGE := $(NOSE) --with-coverage --cover-package=terrascript --cover-erase --cover-branches --cover-html
FLAKE8 := python3 -m flake8

TESTS_BASIC := $(wildcard tests/test_basic_*.py)
TESTS_ISSUES := $(wildcard tests/test_issue*.py)

DEFAULT_GOAL: help

.PHONY: \
	black \
	clean \
	code \
	coverage \
	debug_basic \
	debug_issues \
	flake8 \
	help \
	html \
	install \
	package \
	test \
	test_basic \
	test_black \
	test_issues \
	test_docs

black: clean ## Format Python code with Black to keep style consistent
	black -t py36 .

clean: ## Cleanup temporary / cached files
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseid*

code: clean ## Generate providers shim classes / code
	( cd tools && ./makecode.py )

coverage: clean ## Generate code test coverage
	$(COVERAGE) $(TESTS_BASIC) $(TEST_ISSUES)

debug_basic: clean ## Run basic tests in debug mode
	$(NOSE) --pdb  $(TESTS_BASIC)

debug_issues: clean ## Run tests in debug mode for previous issues
	$(NOSE) --pdb  $(TESTS_ISSUES)

flake8: clean ## Validate code against PEP8
	$(FLAKE8) terrascript/__init__.py #$(TESTS)

help: ## Print this help and exit
	@echo "Available build targets:"
	@grep -e "^[a-zA-Z0-9_-]*: *.*## *" $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}'

html: clean ## Build documentation files
	make -C docs html

install: clean ## Install as python package from sources
	python3 setup.py install --user

package: clean ## Build python package from sources
	python3 setup.py clean
	python3 setup.py sdist

test: clean test_basic test_issues test_docs ## Run all tests

test_basic: clean ## Run basic tests
	$(NOSE) $(TESTS_BASIC)

test_black: clean ## Verify that all Python code are formatted correctly
	black \
		--check \
		--diff \
		--target-version py36 \
		.

test_issues: clean ## Run tests for prevoius issues
	$(NOSE) $(TESTS_ISSUES)

test_docs: ## Run tests for documentation
	(cd docs && make test)
