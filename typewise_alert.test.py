import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(0,0, 35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1,0, 35) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(30, 0,35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(35,0,35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(37,0,35) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', -1) == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 1) == 'NORMAL')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 45) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', -1) == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', -1) == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', 45) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', -1) == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 1) == 'NORMAL')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 35) == 'TOO_HIGH')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 34) == 'NORMAL')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 40) == 'NORMAL')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 45) == 'TOO_HIGH')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', -1) == 'TOO_LOW')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', 45) == 'NORMAL')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', 40) == 'TOO_LOW')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', 50) == 'TOO_HIGH')
    self.assertFalse(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', -1) == 'TOO_LOW')
    self.assertFalse(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 0) == 'TOO_LOW')
    self.assertFalse(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 35) == 'TOO_LOW')
    self.assertFalse(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 40) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 35)=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 30)=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 30)=='NORMAL')
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == "__main__":
  unittest.main()
