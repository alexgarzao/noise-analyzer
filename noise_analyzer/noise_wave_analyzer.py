# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# noise_wave_analyzer.py


class NoiseWaveAnalyzer:
    '''NoiseWaveAnalyzer receives a sample rate value and, based on this value, can decide if the data is a good signal or a noise.
    To decide this, after found the highest value, the analyzer counts, based on the sample_rate, the number of samples to be ignored before the noise values.
    With this same approach, the analyzer knows how much samples are to be considered noise values.
    '''

    # Possible machine states (FSM) when trying to identify noise values.
    ANALYZER_STATE_WAITING_VALUES_INCREASING = 1
    ANALYZER_STATE_SEARCHING_HIGHEST_VALUE = 2
    ANALYZER_STATE_ONE_LOWER_VALUE_FOUND = 3
    ANALYZER_STATE_SEARCHING_ERROR = 4
    ANALYZER_STATE_PROCESSING_ERROR = 5

    def __init__(self, sample_rate, noise_filename=None):
        '''Initialize the object.

        sample_rate: is the limit to decide if a data is a wave or a noise.
        noise_filename: is the csv to be generated with the noise.
        '''
        self.sample_rate = sample_rate
        self.noise_filename = noise_filename
        self.prior_value = 0
        self.state = NoiseWaveAnalyzer.ANALYZER_STATE_WAITING_VALUES_INCREASING
        self.steps = 0
        self.last_file_count = 0
        self.noise_file = None

        self.__new_noise_file()

    def __new_noise_file(self):
        self.last_file_count += 1

        if self.noise_file is not None:
            self.noise_file.close()
            self.noise_file = None

        if self.noise_filename is not None:
            self.noise_file = open('%s_%d.csv' % (self.noise_filename, self.last_file_count), 'w')
        else:
            self.noise_file = None

    def is_noise(self, value):
        '''Verifiy if the value is a noise.

        value: data to be analyzed.
        '''

        # Bellow there is a FSM (Finish state machine) responsible to find noise values.
        # To achieve this, the FSM execute the following steps:
        # 1) Find when the values are been incresed;
        # 2) Find the highest value in the stream (1 hole is supported)
        # 3) Based on the sample_rate parameter, count the samples to be ignored before found the noise;
        # 4) Inform the samples that there are noise values;
        # 5) Go to state 2.

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_WAITING_VALUES_INCREASING:
            if value <= self.prior_value or self.prior_value == 0:
                self.prior_value = value
                return False

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE:
            if value >= self.prior_value:
                self.prior_value = value
                return False

            self.prior_value = value
            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_ONE_LOWER_VALUE_FOUND
            return False

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_ONE_LOWER_VALUE_FOUND:
            if value >= self.prior_value:
                self.prior_value = value
                self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE
                return False

            # Two lower values found. Values are decreasing now.
            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_ERROR
            self.steps = 2

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_ERROR:
            self.steps += 1
            if self.steps <= self.sample_rate / 2:
                return False

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_PROCESSING_ERROR
            self.steps = 0

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_PROCESSING_ERROR:
            self.steps += 1
            if self.steps <= self.sample_rate / 2:
                return True

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE
            self.prior_value = 0
            self.steps = 0
            return False

        assert False, 'Ops... State machine with error :-)'
        return

    def process_values(self, data):
        '''Process values in data to known if its a noise.

        data - list with the numerical values to be analyzed.
        '''
        for value in data:
            if not self.is_noise(value):
                continue

#            print "Noise: %s" % value

            if self.noise_file is not None:
                self.noise_file.write(str(value) + '\n')

    def sample_finished(self):
        '''Notify that the old file noise can be closed, and a new file must be created.
        '''
        self.__new_noise_file()
