
NOSE := nosetests --failed --verbose --with-coverage --cover-package=terrascript --cover-erase --stop --no-byte-compile --logging-level=DEBUG --detailed-errors

TESTS := $(wildcard tests/test_*.py)

all: help

help:
	@echo "make test"
	@echo "make debug"
	@echo "make code"
	@echo "make package"
	@echo "make install"

test:
	$(NOSE) $(TESTS)

debug:
	$(NOSE) --pdb $(TESTS)

code: clean
	./makecode.py

package: clean
	python3 setup.py clean
	python3 setup.py sdist

install: clean
	python3 setup.py install --user

clean:
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseid*
