# Noise analyzer
This analyzer interprets and filters noise in a signal. The noise values are in a previsible place (lower part in the wave). The sample rate is constant, and after found the highest value in a wave, is possible to filter the noise values.

## How to use

Important: The analyzer has been tested only in a Mac OS X system, with python 2.7.

The following softwares are required to correct install and run the analyzer:
* make
* python 2.7
* pip
* git

First of all, clone this repo:

    cd <DIR_TO_PUT_ANALYZER>
    git clone https://github.com/alexgarzao/noise-analyzer
    cd noise-analyzer

After this, run the setup:

    make setup

And run basic tests:

    make tdd

If everything is fine, run BDD tests. To do this, run the analyzer:

    make run

And, in another terminal, run the tests:

    make bdd
