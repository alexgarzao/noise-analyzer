# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# Makefile

tdd:	clean
	nosetests

bdd:	clean
	@echo "\n\nBe sure that the analyzer server is running!!!\n\n"
	cd tests; lettuce; cd ..

run:	clean
	python noise_analyzer/main.py

tests:	clean tdd bdd

checkcode:	lint pep8

lint:
	pylint *.py noise_analyzer/*.py tests/*.py

pep8:
	pep8 *.py noise_analyzer/*.py tests/*.py tests/features/*.py

clean:
	rm -f noise.csv
	rm -f noise_analyzer/*.pyc
	rm -f tests/*.pyc
