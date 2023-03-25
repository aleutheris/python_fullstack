import unittest.mock
from calcpack import Calcmod


class Mul(unittest.TestCase):
    def test_mul(self):
        calcmod = Calcmod(2, 3)
        self.assertEqual(calcmod.mul(), 6)


if __name__ == '__main__':
    unittest.main()
