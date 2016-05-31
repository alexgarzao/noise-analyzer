# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# Makefile

tdd:
	nosetests

run:
	python noise_analyzer/main.py

tests:	tdd

lint:
	pylint *.py noise_analyzer/*.py tests/*.py

pep8:
	pep8 *.py noise_analyzer/*.py tests/*.py

clean:
	rm -f noise.csv
	rm -f noise_analyzer/*.pyc
	rm -f tests/*.pyc
