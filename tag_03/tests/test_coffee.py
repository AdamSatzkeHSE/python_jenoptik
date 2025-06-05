import unittest
from ..oop.coffee import *

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee_instanz = Coffee(100, 100)

    def test_get_coffee(self):
        # Arrange
        # Act
        expected = 200
        actual = self.coffee_instanz.get_coffee()
        # Assert
        self.assertEqual(expected, actual)

