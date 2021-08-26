from my_module import square
import pytest

@pytest.fixture
def input_value():
    return 4

def test_square_give_correct_values(input_value):
     #When
    subject = square(input_value)

    #then
    assert subject == 16