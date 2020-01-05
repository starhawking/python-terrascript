# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "  providers   to generate list_of_providers.rst"
	@echo "  server      to start local documentation web server"

.PHONY: help Makefile providers

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile providerlist
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

providers:
	echo "List of Providers" > list_of_providers.rst
	echo "~~~~~~~~~~~~~~~~~" >> list_of_providers.rst
	sort ../tools/providers.yml | awk -F: '$$1 ~ /name/ { printf("*%s\n",$$2) }' >> list_of_providers.rst

server: 
	python3 -m http.server --directory _build/html/ 8000
