# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# stream_to_number_tests.py

from nose.tools import *
from noise_analyzer import stream_to_number

def test_stream_with_one_value():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	streamData = '123\n'
	remainingData = stn.ProcessStream(streamData)

	assert stn.Size() == 1
	assert remainingData == ''

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert numericalValues[0] == 123


def test_stream_with_two_values():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	streamData = '123\n456\n'
	remainingData = stn.ProcessStream(streamData)

	assert stn.Size() == 2
	assert remainingData == '', 'expected nothing, but remainingData = "%s"' % remainingData

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert numericalValues[0] == 123
	assert numericalValues[1] == 456
