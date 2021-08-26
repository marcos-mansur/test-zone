from my_module import square

import pytest

#convencionally, fixtures are defines in conftest.py, but you can do it in the code too
@pytest.mark.parametrize(           #passes multiple values
    'para_inputs', [                #give it a name, "para_inputs"
    1,5,3,6,8]
)

def test_square_int(para_inputs):
    #When
    subject = square(para_inputs)

    #Than
    assert isinstance(subject, int)