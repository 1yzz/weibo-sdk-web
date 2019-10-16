.PHONY: init
init:
	pip install pipenv --upgrade
	pipenv install --dev

test:
	pytest

publish:
	pip install twine
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg *.egg-info
