# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# Makefile

tdd:
	nosetests

run:
	python noise_analyzer/main.py

clean:
	rm -f noise.csv
	rm -f noise_analyzer/*.pyc
	rm -f tests/*.pyc
