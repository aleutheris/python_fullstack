import unittest.mock
from calcpack import Calcmod


class Sub(unittest.TestCase):
    def test_sub(self):
        calcmod = Calcmod(2, 3)
        self.assertEqual(calcmod.sub(), -1)


if __name__ == '__main__':
    unittest.main()
