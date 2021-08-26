from my_module import square

def test_square_give_correct_values(input_value):
     #When
    subject = square(input_value)

    #then
    assert subject == 16