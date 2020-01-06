
NOSE := nosetests --failed --verbose --no-byte-compile --logging-level=DEBUG --detailed-errors
COVERAGE := $(NOSE) --with-coverage --cover-package=terrascript --cover-erase --cover-branches --cover-html
FLAKE8 := python3 -m flake8

TESTS_BASIC := $(wildcard tests/test_basic_*.py)
TESTS_ISSUES := $(wildcard tests/test_issue*.py)

all: help

help:
	@echo "make test|test_basic|test_issues|test_docs"
	@echo "make coverage"
	@echo "make debug"
	@echo "make code"
	@echo "make package"
	@echo "make install"

# Test targets
# 
test: clean test_basic test_issues test_docs

test_basic: clean
	$(NOSE) $(TESTS_BASIC)

test_issues: clean
	$(NOSE) $(TESTS_ISSUES)

test_docs:
	(cd docs && make test)

coverage: clean
	$(COVERAGE) $(TESTS_BASIC) $(TEST_ISSUES)

flake8: clean
	$(FLAKE8) terrascript/__init__.py #$(TESTS)

debug:
	$(NOSE) --pdb $(TESTS)

code: clean
	( cd tools && ./makecode.py )

package: clean
	python3 setup.py clean
	python3 setup.py sdist

install: clean
	python3 setup.py install --user
	
html: clean
	make -C docs html

clean:
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseid*
