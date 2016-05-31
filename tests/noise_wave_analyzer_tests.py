# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# noise_wave_analyzer_tests.py

from nose.tools import *
from noise_analyzer import noise_wave_analyzer

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_signal_is_noise():
	analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
	assert analyzer.IsNoise(50) == False

	assert analyzer.IsNoise(55) == False # Highest
	assert analyzer.IsNoise(48) == False
	assert analyzer.IsNoise(40) == False
	assert analyzer.IsNoise(30) == False

	assert analyzer.IsNoise(20) == True # start noise
	assert analyzer.IsNoise(18) == True
	assert analyzer.IsNoise(22) == True
	assert analyzer.IsNoise(28) == True # end noise

	assert analyzer.IsNoise(32) == False
	assert analyzer.IsNoise(41) == False
	assert analyzer.IsNoise(49) == False
	assert analyzer.IsNoise(52) == False

	assert analyzer.IsNoise(54) == False # Highest
	assert analyzer.IsNoise(48) == False
	assert analyzer.IsNoise(40) == False
	assert analyzer.IsNoise(30) == False

	assert analyzer.IsNoise(20) == True # start noise
	assert analyzer.IsNoise(18) == True
	assert analyzer.IsNoise(22) == True
	assert analyzer.IsNoise(28) == True # end noise

	assert analyzer.IsNoise(32) == False
	assert analyzer.IsNoise(41) == False
	assert analyzer.IsNoise(49) == False
	assert analyzer.IsNoise(51) == False

	assert analyzer.IsNoise(54) == False # Highest
	assert analyzer.IsNoise(48) == False
	assert analyzer.IsNoise(40) == False
	assert analyzer.IsNoise(30) == False

	assert analyzer.IsNoise(20) == True # start noise
	assert analyzer.IsNoise(18) == True
	assert analyzer.IsNoise(22) == True
	assert analyzer.IsNoise(28) == True # end noise

	assert analyzer.IsNoise(32) == False
	assert analyzer.IsNoise(41) == False
	assert analyzer.IsNoise(49) == False
	assert analyzer.IsNoise(50) == False

	assert analyzer.IsNoise(54) == False # Highest
	assert analyzer.IsNoise(48) == False
	assert analyzer.IsNoise(40) == False
	assert analyzer.IsNoise(30) == False

#def test_signal_is_valid():
#	analyzer = NoiseWaveAnalyzer.NoiseWaveAnalyzer(sample_rate=8)
#	assert analyzer.IsNoise(101) == False
#	assert analyzer.IsNoise(200) == False
