# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# noise-analyzer_tests.py

from nose.tools import *
from noise_analyzer import NoiseWaveAnalyzer

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_signal_is_noise():
	analyzer = NoiseWaveAnalyzer.NoiseWaveAnalyzer(threshold=100)
	assert analyzer.IsNoise(50) == True
	assert analyzer.IsNoise(100) == True

def test_signal_is_valid():
	analyzer = NoiseWaveAnalyzer.NoiseWaveAnalyzer(threshold=100)
	assert analyzer.IsNoise(101) == False
	assert analyzer.IsNoise(200) == False
