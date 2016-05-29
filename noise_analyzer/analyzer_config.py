# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# analyzer_config.py

class AnalyzerConfig:
	'''Class responsible to load and keep the analyzer config.

	Nowadays, all configs are hard coded here, but it will change when necessary :-)
	'''


	def __init__(self):
		'''Initialize default values.
		'''
		self.Threshold = 100


	def load(self):
		'''Load the configuration values from the config file.
		'''
		pass
