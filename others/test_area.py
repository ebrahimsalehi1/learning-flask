import unittest
from others.area import area

class TestArea(unittest.TestCase):
    def test_area_natural_number(self):
        # self.assertEqual(1==1,False)
        self.assertAlmostEqual(area(0),0)
        self.assertAlmostEqual(area(1),1)

    def test_area_neg_number(self):
        self.assertEqual(area(-10),100)

    def test_area_string(self):
        self.assertAlmostEqual(area("10sds"),-1)


if __name__ == '__main__':
    unittest.main()
