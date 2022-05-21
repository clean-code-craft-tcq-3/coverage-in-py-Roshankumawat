import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 40) == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', 45) == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
