# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# noise_wave_analyzer_tests.py

from nose.tools import *
from noise_analyzer import noise_wave_analyzer


def test_start_noise_sr_6_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=6)
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False

    assert analyzer.IsNoise(30) is True     # start noise


def test_start_noise_sr_8_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise


def test_two_waves_sr_8_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(52) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(51) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False


def test_two_waves_sr_8_values_decreasing_is_ok():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)

    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is False    # start noise, but highest value not found yet
    assert analyzer.IsNoise(18) is False
    assert analyzer.IsNoise(22) is False
    assert analyzer.IsNoise(28) is False    # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(52) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(51) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False


def test_two_waves_sr_8_with_one_hole():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(47) is False
    assert analyzer.IsNoise(45) is False    # Hole
    assert analyzer.IsNoise(52) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(34) is False
    assert analyzer.IsNoise(31) is False    # Hole
    assert analyzer.IsNoise(44) is False
    assert analyzer.IsNoise(47) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False


def test_two_waves_sr_8_with_two_holes():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(47) is False
    assert analyzer.IsNoise(45) is False    # Hole
    assert analyzer.IsNoise(52) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(34) is False
    assert analyzer.IsNoise(31) is False    # Hole
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(47) is False    # Hole

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False


def test_two_waves_sr_8_with_one_big_hole():
    analyzer = noise_wave_analyzer.NoiseWaveAnalyzer(sample_rate=8)
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(55) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(47) is False
    assert analyzer.IsNoise(45) is False    # Hole
    assert analyzer.IsNoise(52) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(34) is False
    assert analyzer.IsNoise(27) is False    # Big hole
    assert analyzer.IsNoise(31) is False
    assert analyzer.IsNoise(47) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False

    assert analyzer.IsNoise(20) is True     # start noise
    assert analyzer.IsNoise(18) is True
    assert analyzer.IsNoise(22) is True
    assert analyzer.IsNoise(28) is True     # end noise

    assert analyzer.IsNoise(32) is False
    assert analyzer.IsNoise(41) is False
    assert analyzer.IsNoise(49) is False
    assert analyzer.IsNoise(50) is False

    assert analyzer.IsNoise(54) is False    # Highest
    assert analyzer.IsNoise(48) is False
    assert analyzer.IsNoise(40) is False
    assert analyzer.IsNoise(30) is False
