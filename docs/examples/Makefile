
PYTHON2TFJSON := ../../tools/python2tfjson.py

PYTHON_SOURCES = $(wildcard *.py)
PYTHON_OUTPUT = $(patsubst %.py, %.tf.json, $(PYTHON_SOURCES))

.PHONY: python2tfjson

all: python2tfjson

python2tfjson: $(PYTHON_OUTPUT)

%.tf.json: %.py
	[ -d `basename $< .py` ] || mkdir -v `basename $< .py`
	python3 $(PYTHON2TFJSON) $< > `basename $< .py`/$@
	( cd `basename $< .py` && terraform init )
	( cd `basename $< .py` && terraform validate )

clean:
	rm -fv $(PYTHON_OUTPUT)


