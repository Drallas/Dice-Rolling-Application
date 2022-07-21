import unittest

import dice
import main

# Check tests via: python3 -m unittest discover


class TestInput(unittest.TestCase):
    '''check if input outside of range is handled correctly and raises SystemExit and value between 1 and 6 is returned.'''

    def test_input(self):
        with self.assertRaises(SystemExit):
            check = [-1, 0, 7, 1.1]
            for i in check:
                main.check_input(i)


class TestRollDice(unittest.TestCase):
    '''Check if roll_dice() returns a random number between 1 and 6.'''

    def test_roll_dice(self):
        for i in range(100):
            assert 1 <= dice.roll_dice() <= 6
