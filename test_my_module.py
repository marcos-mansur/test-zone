from my_module import square

def test_square_give_correct_values():
     #When
    subject = square(2)

    #then
    assert subject == 5