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
	assert remainingData == '', 'expected nothing, but remainingData = "%s"' % remainingData

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert len(numericalValues) == 1
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
	assert len(numericalValues) == 2
	assert numericalValues[0] == 123
	assert numericalValues[1] == 456

def test_stream_with_one_complete_and_one_incomplete_value():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	remainingData = stn.ProcessStream('123\n456')
	assert stn.Size() == 1
	assert remainingData == '456', 'expected 456, but remainingData = "%s"' % remainingData

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert len(numericalValues) == 1
	assert numericalValues[0] == 123

def test_stream_with_one_incomplete_value():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	remainingData = stn.ProcessStream('123')
	assert stn.Size() == 0
	assert remainingData == '123', 'expected 123, but remainingData = "%s"' % remainingData

	numericalValues = stn.GetNumericalValues()
	assert len(numericalValues) == 0

def test_stream_with_one_value_but_starting_with_delimiter():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	streamData = '\n123\n'
	remainingData = stn.ProcessStream(streamData)

	assert stn.Size() == 1
	assert remainingData == ''

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert len(numericalValues) == 1
	assert numericalValues[0] == 123

def test_stream_with_one_value_but_in_two_blocks():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	remainingData = stn.ProcessStream('12')
	assert stn.Size() == 0
	assert remainingData == '12', 'expected 12, but remainingData = "%s"' % remainingData

	remainingData = stn.ProcessStream('3\n')
	assert stn.Size() == 1
	assert remainingData == '', 'expected nothing, but remainingData = "%s"' % remainingData

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert len(numericalValues) == 1
	assert numericalValues[0] == 123

def test_stream_with_one_value_but_in_three_blocks():
	stn = stream_to_number.StreamToNumber()
	assert stn.Size() == 0

	remainingData = stn.ProcessStream('12')
	assert stn.Size() == 0
	assert remainingData == '12', 'expected 12, but remainingData = "%s"' % remainingData

	remainingData = stn.ProcessStream('3')
	assert stn.Size() == 0
	assert remainingData == '123', 'expected 123, but remainingData = "%s"' % remainingData

	remainingData = stn.ProcessStream('\n')
	assert stn.Size() == 1
	assert remainingData == '', 'expected nothing, but remainingData = "%s"' % remainingData

	numericalValues = stn.GetNumericalValues()
	assert stn.Size() == 0
	assert len(numericalValues) == 1
	assert numericalValues[0] == 123
