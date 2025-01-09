
import pytest
from src.main import add

@pytest.mark.skip('for no reason')
def test_add():
    # Arrange
    x = 2
    y = 3
    expected_result = 5

    # Act
    result = add(x, y)
    
    # Assert
    assert result == expected_result

