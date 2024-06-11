class ValueTooHighError (Exception):
    pass

def test_value (x):
    if x > 100:
        raise ValueTooHighError ('Value is too high')
    
    test_value(200)


    try:
        test_value (200)
    except ValueTooHighError as e:
        print (e)
    

