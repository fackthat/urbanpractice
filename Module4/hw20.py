def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function() # возвращает знаение print()
inner_function() # name 'inner_function' is not defined