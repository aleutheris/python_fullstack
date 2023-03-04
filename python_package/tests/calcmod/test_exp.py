import unittest
from unittest.mock import patch
from calcpack import Calcmod
from calcpack import Expmod, expmod


class Exp(unittest.TestCase):
    @patch.object(expmod, 'os')
    @patch.object(Expmod, 'exp')
    def test_exp(self, mock_exp, mock_os):
        mock_exp.return_value = 8

        calcmod = Calcmod(2, 6)
        self.assertEqual(calcmod.exp(), 8)


if __name__ == '__main__':
    unittest.main()
