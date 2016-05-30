# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# NoiseWaveAnalyzer.py

class NoiseWaveAnalyzer:
	'''NoiseWaveAnalyzer receives a threshold and, based on this value, can decide if the data is a good signal or a noise.
	'''

	def __init__(self, threshold):
		'''Initialize the object.

		threshold: is the limit to decide if a data is a wave or a noise.
		'''
		self.Threshold = threshold

	def IsNoise(self, value):
		'''Verifiy if the value is a noise.

		value: data to be analyzed.
		'''
		return value <= self.Threshold


	def ProcessValues(self, data):
		'''Process values in data to known if its a noise.

		data - list with the numerical values to be analyzed.
		'''
		for value in data:
			if not self.IsNoise(value):
				continue

			print "Noise: %s" % value
