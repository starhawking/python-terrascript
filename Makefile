

NOSE := python3 -m nose --failed --verbose --with-coverage --cover-package=terrascript --stop --no-byte-compile --logging-level=DEBUG --detailed-errors

# The tests must be executed in this order!!
TESTS := tests/test.py tests/test_providers.py 
TEST_ISSUES := $(wildcard tests/test_issue*.py)

NOSEIDS = $(shell ./.read_noseids.py)


all: help

help:
	@echo "make test"
	@echo "make test_issues"
	@echo "make debug"
	@echo "make debug_issues"
	@echo "make code"
	@echo "make package"
	@echo "make install"

noseids:
	python3 -m nose --collect-only --with-id --id-file=.noseids $(TESTS)

test2:
	$(NOSE) --processes=165 --process-restartworker --process-timeout=30 $(TESTS)

test:
	$(NOSE) --with-id $(TESTS) $(TEST_ISSUES)

test_issues:
	$(NOSE) --with-id $(TEST_ISSUES)

debug:
	$(NOSE) --with-id --pdb $(TESTS) $(TEST_ISSUES)

debug_issues:
	$(NOSE) --with-id --pdb $(TEST_ISSUES)

code: clean
	./makecode.py

package: clean
	python3 setup.py clean
	python3 setup.py sdist

install: clean
	python3 setup.py install

clean:
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseid*
