.PHONY: init
init:
	pip install pipenv --upgrade
	pipenv install --dev

test:
	pytest

publish:
	pip install twine
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg *.egg-info
