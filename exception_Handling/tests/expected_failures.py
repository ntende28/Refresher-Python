import unittest

class FeatureTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_broken_feature(self):
        raise Exception("This test is going to fail")

unittest.main()