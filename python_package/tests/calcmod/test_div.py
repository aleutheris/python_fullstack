import unittest.mock
from calcpack import Calcmod


class Div(unittest.TestCase):
    def test_div(self):
        calcmod = Calcmod(2, 3)
        self.assertEqual(calcmod.div(), 0.6666666666666666)


if __name__ == '__main__':
    unittest.main()
