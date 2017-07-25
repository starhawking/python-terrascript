

NOSE := nosetests --failed --verbose --with-coverage --cover-package=terrascript --stop --with-id --no-byte-compile --logging-level=DEBUG


all: help

help:
	@echo "make test"
	@echo "make debug"
	@echo "make code"
	@echo "make package"

test:
	$(NOSE) tests/*

debug:
	$(NOSE) --pdb tests/*

code: clean update
	./makecode.py

update:
	git submodule update --recursive

package: clean code
	python3 setup.py clean
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal


clean:
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseids
