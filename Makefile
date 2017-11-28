

NOSE := nosetests --failed --verbose --with-coverage --cover-package=terrascript --stop --with-id --no-byte-compile --logging-level=DEBUG

# The tests must be executed in this order!!
TESTS := tests/test.py tests/test_providers.py


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
	python3 setup.py install

clean:
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseids
