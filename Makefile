.PHONY: docs

dev:
	# Install recommended dev packages
	pip install -U pip setuptools nose coverage wheel

test:
	# This runs all of the tests. To run an individual test, run nosetests with
	# a module path specified
	nosetests tests

coverage:
	# Run the test suite with coverage enabled
	nosetests --verbose --with-coverage --cover-package subler tests

publish:
	# Register and upload packages to PyPi, then clean up
	python setup.py register
	python setup.py sdist upload
	rm MANIFEST
	rm -rf dist
	rm -rf subler.egg-info

docs-init:
	# Install packages required to build documentation
	pip install Sphinx

docs:
	# Build documentation
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"