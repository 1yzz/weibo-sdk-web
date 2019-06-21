.PHONY: test
test:
	pytest

publish:
	pip install twine
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg *.egg-info
