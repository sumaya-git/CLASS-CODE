import unittest

from unittest.mock import patch

from src.calc import addition, multiply_2

class MockingTestCase(unittest.TestCase):
    def test_addition_passed(self):
        x = 1
        y = 4
        z = 2

        expected_result = 7
        result = addition(x, y, z)

        # Assert
        self.assertEqual(
            expected_result, result, f"Expected {expected_result}, but got {result}"
        )

    def test_addition_incorrect_input(self):
        # Arrange
        x = []
        y = "4"

        with self.assertRaises(TypeError):
            addition(x, y)

    @patch('src.calc.addition')
    def test_multiply_2_passed(self, addition_mock):
        x = 1
        y = 3
        excepted_result = 3

        addition_mock.side_effect = [1, 2, 3]
        # addition_mock.return_value = 2

        #act 
        result = multiply_2(x,y)

        #assert
        self.assertEqual(excepted_result, result, f'Expected {excepted_result}, but got {result}.')


    def test_multiply_2_with_incorrect_input(self):
        x ='4'
        y = 4


        with patch('src.calc.addition') as addition_mock:
            addition_mock.side_effect = TypeError

            with self.assertRaises(TypeError):
                multiply_2(x,y)

    @patch('src.calc.input')
    def test_ask_username_input(self, input_mock):
        excepted_name = 'kevin'
        input_mock.return_value = 'kevin'

        result = ask_username()

        self.assertEqual(excepted_name, result)

        input.assert_called_once_with('Enter your name:')            

