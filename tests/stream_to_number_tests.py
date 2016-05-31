# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# stream_to_number_tests.py

from nose.tools import *
from noise_analyzer import stream_to_number


def test_stream_with_one_value():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    stream_data = '123\n'
    remaining_data = stn.process_stream(stream_data)
    assert stn.size() == 1
    assert remaining_data == '', 'expected nothing, but remaining_data = "%s"' % remaining_data

    numerical_values = stn.get_numerical_values()
    assert stn.size() == 0
    assert len(numerical_values) == 1
    assert numerical_values[0] == 123


def test_stream_with_two_values():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    stream_data = '123\n456\n'
    remaining_data = stn.process_stream(stream_data)
    assert stn.size() == 2
    assert remaining_data == '', 'expected nothing, but remaining_data = "%s"' % remaining_data

    numerical_values = stn.get_numerical_values()
    assert stn.size() == 0
    assert len(numerical_values) == 2
    assert numerical_values[0] == 123
    assert numerical_values[1] == 456


def test_stream_with_one_complete_and_one_incomplete_value():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    remaining_data = stn.process_stream('123\n456')
    assert stn.size() == 1
    assert remaining_data == '456', 'expected 456, but remaining_data = "%s"' % remaining_data

    numerical_values = stn.get_numerical_values()
    assert stn.size() == 0
    assert len(numerical_values) == 1
    assert numerical_values[0] == 123


def test_stream_with_one_incomplete_value():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    remaining_data = stn.process_stream('123')
    assert stn.size() == 0
    assert remaining_data == '123', 'expected 123, but remaining_data = "%s"' % remaining_data

    numerical_values = stn.get_numerical_values()
    assert len(numerical_values) == 0


def test_stream_with_one_value_but_starting_with_delimiter():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    stream_data = '\n123\n'
    remaining_data = stn.process_stream(stream_data)

    assert stn.size() == 1
    assert remaining_data == ''

    numerical_values = stn.get_numerical_values()
    assert stn.size() == 0
    assert len(numerical_values) == 1
    assert numerical_values[0] == 123


def test_stream_with_one_value_but_in_two_blocks():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    remaining_data = stn.process_stream('12')
    assert stn.size() == 0
    assert remaining_data == '12', 'expected 12, but remaining_data = "%s"' % remaining_data

    remaining_data = stn.process_stream('3\n')
    assert stn.size() == 1
    assert remaining_data == '', 'expected nothing, but remaining_data = "%s"' % remaining_data

    numerical_values = stn.get_numerical_values()
    assert stn.size() == 0
    assert len(numerical_values) == 1
    assert numerical_values[0] == 123


def test_stream_with_one_value_but_in_three_blocks():
    stn = stream_to_number.StreamToNumber()
    assert stn.size() == 0

    remaining_data = stn.process_stream('12')
    assert stn.size() == 0
    assert remaining_data == '12', 'expected 12, but remaining_data = "%s"' % remaining_data

    remaining_data = stn.process_stream('3')
    assert stn.size() == 0
    assert remaining_data == '123', 'expected 123, but remaining_data = "%s"' % remaining_data

    remaining_data = stn.process_stream('\n')
    assert stn.size() == 1
    assert remaining_data == '', 'expected nothing, but remaining_data = "%s"' % remaining_data

    numerical_values = stn.get_numerical_values()
    assert stn.size() == 0
    assert len(numerical_values) == 1
    assert numerical_values[0] == 123
