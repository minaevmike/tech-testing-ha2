#!/usr/bin/env python2

import sys
import unittest
from tests.example_test import SeleniumTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(SeleniumTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
