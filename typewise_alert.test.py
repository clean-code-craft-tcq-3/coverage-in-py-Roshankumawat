import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', -1) == 'TOO_LOW')
    self.assertFalse(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 0) == 'TOO_LOW')
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
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == "__main__":
  unittest.main()
