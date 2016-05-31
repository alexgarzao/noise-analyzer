# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# noise_wave_analyzer.py


class NoiseWaveAnalyzer:
    '''NoiseWaveAnalyzer receives a sample rate value and, based on this value, can decide if the data is a good signal or a noise.
    To decide this, after found the highest value, the analyzer count, based on the sample_rate, the number of samples to be ignored before the noise values.
    With this same approach, the analyzer knows how much samples are to be considered noise values.
    '''

    # Possible machine states (FSM) when trying to identify noise values.
    ANALYZER_STATE_WAITING_VALUES_INCREASING = 1
    ANALYZER_STATE_SEARCHING_HIGHEST_VALUE = 2
    ANALYZER_STATE_SEARCHING_ERROR = 3
    ANALYZER_STATE_PROCESSING_ERROR = 4

    def __init__(self, sample_rate, noise_filename=None):
        '''Initialize the object.

        sample_rate: is the limit to decide if a data is a wave or a noise.
        noise_filename: is the csv to be generated with the noise.
        '''
        if noise_filename != None:
            self.noise_file = open(noise_filename,'a')
        else:
            self.noise_file = None
        self.SampleRate = sample_rate
        self.priorValue = 0
        self.state = NoiseWaveAnalyzer.ANALYZER_STATE_WAITING_VALUES_INCREASING
        self.steps = 0


    def IsNoise(self, value):
        '''Verifiy if the value is a noise.

        value: data to be analyzed.
        '''

        # Bellow there is a FSM (Finish state machine) responsible to find noise values.
        # To achieve this, the FSM execute the following steps:
        # 1) Find when the values are been incresed;
        # 2) Find the highest value in the stream;
        # 3) Based on the sample_rate parameter, count the samples to be ignored before found the noise;
        # 4) Inform the samples that there are noise values;
        # 5) Go to state 2.

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_WAITING_VALUES_INCREASING:
            if value <= self.priorValue or self.priorValue == 0:
                self.priorValue = value
                return False

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE:
            if value >= self.priorValue:
                self.priorValue = value
                return False

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_ERROR
            self.steps = 1

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_ERROR:
            self.steps += 1
            if self.steps <= self.SampleRate / 2:
                return False

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_PROCESSING_ERROR
            self.steps = 0

        if self.state == NoiseWaveAnalyzer.ANALYZER_STATE_PROCESSING_ERROR:
            self.steps += 1
            if self.steps <= self.SampleRate / 2:
                return True

            self.state = NoiseWaveAnalyzer.ANALYZER_STATE_SEARCHING_HIGHEST_VALUE
            self.priorValue = 0
            return False

        assert False, 'Ops... State machine with error :-)'
        return


    def ProcessValues(self, data):
        '''Process values in data to known if its a noise.

        data - list with the numerical values to be analyzed.
        '''
        for value in data:
            if not self.IsNoise(value):
                continue

#            print "Noise: %s" % value

            if self.noise_file != None:
                self.noise_file.write(str(value) + '\n')
