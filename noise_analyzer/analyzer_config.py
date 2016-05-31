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
        self.sample_rate = 50
        self.port = 55678                          # Arbitraty port.
        self.noise_filename = 'noise_connection_'

    def load(self):
        '''Load the configuration values from the config file.
        '''
        pass
