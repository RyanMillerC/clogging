.PHONY: install test

install:
	python setup.py install

test:
	python -m pytest
