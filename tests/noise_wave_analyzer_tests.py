# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# noise_wave_analyzer_tests.py

from nose.tools import *
from noise_analyzer import noise_wave_analyzer


def test_start_noise_sr_6_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=6)
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False

    assert analyzer.is_noise(30) is True     # start noise


def test_start_noise_sr_8_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise


def test_two_waves_sr_8_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(52) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(51) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False


def test_two_waves_sr_8_values_decreasing_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)

    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is False    # start noise, but highest value not found yet
    assert analyzer.is_noise(18) is False
    assert analyzer.is_noise(22) is False
    assert analyzer.is_noise(28) is False    # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(52) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(51) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False


def test_two_waves_sr_8_with_one_hole():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(47) is False
    assert analyzer.is_noise(45) is False    # Hole
    assert analyzer.is_noise(52) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(34) is False
    assert analyzer.is_noise(31) is False    # Hole
    assert analyzer.is_noise(44) is False
    assert analyzer.is_noise(47) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False


def test_two_waves_sr_8_with_two_holes():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(47) is False
    assert analyzer.is_noise(45) is False    # Hole
    assert analyzer.is_noise(52) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(34) is False
    assert analyzer.is_noise(31) is False    # Hole
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(47) is False    # Hole

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False


def test_two_waves_sr_8_with_one_big_hole():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(55) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(47) is False
    assert analyzer.is_noise(45) is False    # Hole
    assert analyzer.is_noise(52) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(34) is False
    assert analyzer.is_noise(27) is False    # Big hole
    assert analyzer.is_noise(31) is False
    assert analyzer.is_noise(47) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False

    assert analyzer.is_noise(20) is True     # start noise
    assert analyzer.is_noise(18) is True
    assert analyzer.is_noise(22) is True
    assert analyzer.is_noise(28) is True     # end noise

    assert analyzer.is_noise(32) is False
    assert analyzer.is_noise(41) is False
    assert analyzer.is_noise(49) is False
    assert analyzer.is_noise(50) is False

    assert analyzer.is_noise(54) is False    # Highest
    assert analyzer.is_noise(48) is False
    assert analyzer.is_noise(40) is False
    assert analyzer.is_noise(30) is False
