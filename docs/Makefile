# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

DEFAULT_GOAL: help

.PHONY: \
	clean \
	help \
	html \
	Makefile \
	providers \
	server \
	test

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile providerlist
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

help: ## Print this help and exit
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo -e "\nAvailable docs targets:"
	@grep -e "^[a-zA-Z0-9_-]*: *.*## *" $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}'

clean: ## Remove build documentation files
	rm -rf _build

html: ## Build all documentation as HTML
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

providers: ## Generate list of providers into list_of_providers.rst
	echo "List of Providers" > list_of_providers.rst
	echo "~~~~~~~~~~~~~~~~~" >> list_of_providers.rst
	sort ../tools/providers.yml | awk -F: '$$1 ~ /name/ { printf("*%s\n",$$2) }' >> list_of_providers.rst

server: ## Spawn documentation web server on port 8000
	python3 -m http.server --directory _build/html/ 8000

test: ## Generate Terraform json from examples to validate syntax
	make -C tutorials/
