'''
A test fixture is a mechanism for ensuring proper test setup (putting tests into a known 
state) and test teardown (restoring the state prior to the test running). 
'''
import unittest

def power_cycle_device():
    print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    power_cycle_device()

  def test_feature_a(self):
    print('Testing Feature A')

  def test_feature_b(self):
    print('Testing Feature B')

  @classmethod
  def tearDownClass(cls):
    power_cycle_device()


unittest.main()