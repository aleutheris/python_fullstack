import unittest.mock
from calcpack import Calcmod


class Add(unittest.TestCase):
    def test_add(self):
        calcmod = Calcmod(2, 3)
        self.assertEqual(calcmod.add(), 5)


if __name__ == '__main__':
    unittest.main()
