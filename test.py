import unittest

import dice
import main

# Check tests via: python3 -m unittest discover

# Test 1: check if input outside of range is handled correctly and raises SystemExit and value between 1 and 6 is returned.


class TestDice(unittest.TestCase):
    def test_input(self):
        assert main.check_input(1) == 1
        assert main.check_input(6) == 6

        with self.assertRaises(SystemExit):
            check = [0, -1, 7, "a"]
            for i in check:
                main.check_input(i)


# Test 2: Check if roll_dice() returns a random number between 1 and 6.
class TestRollDice(unittest.TestCase):
    def test_roll_dice(self):
        for i in range(100):
            assert 1 <= dice.roll_dice() <= 6
