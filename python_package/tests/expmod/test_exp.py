import unittest.mock
from calcpack import Expmod


class Exp(unittest.TestCase):
    def test_exp(self):
        expmod = Expmod(2, 3)
        self.assertEqual(expmod.exp(), 8)


if __name__ == '__main__':
    unittest.main()
