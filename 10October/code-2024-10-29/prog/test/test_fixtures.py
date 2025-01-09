import pytest

#Fixture
@pytest.fixture()
def data_set():
    return list(range(10))

#Test
def test_data_len(data_set):
    assert len(data_set) == 10