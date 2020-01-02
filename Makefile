
NOSE := nosetests --failed --verbose --no-byte-compile --logging-level=DEBUG --detailed-errors

COVERAGE := $(NOSE) --with-coverage --cover-package=terrascript --cover-erase --cover-branches --cover-html

TESTS := $(wildcard tests/test_*.py)

all: help

help:
	@echo "make test"
	@echo "make coverage"
	@echo "make debug"
	@echo "make code"
	@echo "make package"
	@echo "make install"

test:
	$(NOSE) $(TESTS)

coverage:
	$(COVERAGE) $(TESTS)

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
