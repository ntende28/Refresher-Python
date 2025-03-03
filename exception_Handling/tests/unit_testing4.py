'''

assertRaises - It takes an exception type as its first argument, a function reference
				 as its second, and an arbitrary number of arguments as the rest

assertWarns   - It takes a warning type as its first argument, a function reference as 
				its second, and an arbitrary number of arguments for the rest
'''
import unittest
import alerts

# Write your code here:
class SystemAlertTests(unittest.TestCase):
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)

  
unittest.main()