PYTHON2TFJSON := ../../tools/python2tfjson.py

PYTHON_SOURCES = $(wildcard *.py)
PYTHON_OUTPUT = $(patsubst %.py, %.tf.json, $(PYTHON_SOURCES))

DEFAULT_GOAL: python2tfjson

.PHONY: \
	clean \
	help \
	python2tfjson

%.tf.json: %.py
	[ -d `basename $< .py` ] || mkdir -v `basename $< .py`
	python3 $(PYTHON2TFJSON) $< > `basename $< .py`/$@
	( cd `basename $< .py` && terraform init )
	( cd `basename $< .py` && terraform validate )

clean:
	rm -fv $(PYTHON_OUTPUT)

help: ## Print this help and exit
	@echo "Available build targets:"
	@grep -e "^[a-zA-Z0-9_-]*: *.*## *" $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}'

python2tfjson: $(PYTHON_OUTPUT) ## Generate Terraform json configuration from tutorials