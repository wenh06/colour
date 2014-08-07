# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_correction.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`colour.colorimetry.correction` module.

**Others:**

"""

from __future__ import unicode_literals

import numpy as np
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.colorimetry import (
    SpectralPowerDistribution,
    bandpass_correction_stearns1988)

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["SPD_DATA",
           "BANDPASS_CORRECTED_STEARNS_SPD_DATA",
           "TestBandpassCorrectionStearns1988"]

SPD_DATA = np.array([
    9.3700,
    12.3200,
    12.4600,
    9.5100,
    5.9200,
    4.3300,
    4.2900,
    3.8800,
    4.5100,
    10.9200,
    27.5000,
    49.6700,
    69.5900,
    81.7300,
    88.1900,
    86.0500])

BANDPASS_CORRECTED_STEARNS_SPD_DATA = np.array([
    9.12515,
    12.57355255,
    12.69542514,
    9.54357971,
    5.75121288,
    4.21535933,
    4.33022518,
    3.79034131,
    4.03770167,
    10.11509076,
    27.10283747,
    49.88971449,
    70.2175037,
    82.14935719,
    88.88373581,
    85.87238])


class TestBandpassCorrectionStearns1988(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.correction.bandpass_correction_stearns1988`
    definition units tests methods.
    """

    def test_bandpass_correction_stearns1988(self):
        """
        Tests :func:`colour.colorimetry.correction.bandpass_correction_stearns1988`
        definition.
        """

        spd = SpectralPowerDistribution(
            "Spd", dict(tuple(zip(range(len(SPD_DATA)), SPD_DATA))))

        np.testing.assert_almost_equal(
            bandpass_correction_stearns1988(spd).values,
            BANDPASS_CORRECTED_STEARNS_SPD_DATA)


if __name__ == "__main__":
    unittest.main()
