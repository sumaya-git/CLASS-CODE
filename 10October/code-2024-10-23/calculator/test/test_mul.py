import unittest

from src.calc import multiply
class TestMultipicationTestCase(unittest.TestCase):
    def test_mul_two_numbers(self):
        #Arrange
        x = 4
        y = 3
        expected_result = 12

        #act
        result = multiply(x,y)

        #Assert
        assert result == expected_result, f'Expected {expected_result}, but got {result}.'

    def test_mul_with_str_numbers(self):
        # Arrange
        x = '4'
        y = '2'
        expected_result = 8

        #act
        result = multiply(x,y)

        #Assert
        self.assertEqual(result, expected_result,f'Expected {expected_result}, but got {result}')

        # self.assertTrue(result == expected_result,f'Expected {expected_result}, but got {result}')

        # assert result == expected_result, f'Expected {expected_result}, but got {result}.'

if __name__ == '__main__':
    unittest.main()