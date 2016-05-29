# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# NoiseWaveAnalyzer.py

class NoiseWaveAnalyzer():
	def __init__(self, threshold):
		self.Threshold = threshold
	def IsNoise(self, value):
		return value <= self.Threshold