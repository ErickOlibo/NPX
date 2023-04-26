#!/usr/bin/env make

# Version of Python
PYTHON ?= python3

# To define targets in each directory under the src/
define FOREACH
	for DIR in src/*; do \
		$(MAKE) -C $$DIR $(1); \
	done
endef

# ---------------------------------------------------------
# Different Keywords for common commands
#

run: main.py
	@printf "This Starts up the NPX App\n"
	$(PYTHON) src/app/main.py


install: requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

# Metrics and Code Analysis Tools
coverage:
	$(PYTHON) -m coverage run -m unittest discover src/app/
	coverage report
	coverage html

flake8:
	for f in src/app/*.py ; do flake8 $${f} ; done
	for f in src/app/gui/*.py ; do flake8 $${f} ; done


pylint:
	for f in src/app/*.py; do \
		if grep -q test_ "$${f}"; then \
			continue; \
		else \
			pylint $${f}; \
		fi \
	done
