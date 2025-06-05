import unittest
from ..oop.roboter_2 import Robot, RobotException

class TestRobotFunctions(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("Marvin", 0, 0, "north")

    @unittest.skip("Heute nicht")
    def test_move(self):
        # Arrange
        expected = [0, 10]
        # Act
        self.robot.move(10)
        actual = self.robot.position
        # Assert
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_robot_error(self):
        # arrange

        # act
        self.robot.robot_error()
        # assert
        self.assertRaises(RobotException)