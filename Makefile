

NOSE := nosetests --failed --verbose --with-coverage --cover-package=terrascript --stop --with-id --no-byte-compile


all: help

help:
	@echo "make test"
	@echo "make debug"
	@echo "make code"

test:
	$(NOSE) tests/*

debug:
	$(NOSE) --pdb tests/*

code:
	./makecode.py

clean:
	rm -f tests/*.pyc
	rm -f terrascript/*.pyc
	rm -f terrascript/*/*.pyc
	rm -f .coverage
	rm -f .noseids
