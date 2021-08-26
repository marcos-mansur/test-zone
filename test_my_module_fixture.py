from my_module import square

def test_square_int(input_value):
    #When
    subject = square(input_value)

    #Than
    assert isinstance(subject, int)