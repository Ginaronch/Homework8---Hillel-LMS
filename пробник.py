def add_one(some_list):
    string = ''
    some_list = (string.join(str(element) for element in some_list))
    some_list = str(int(some_list) + 1)
    some_list = [int(digit) for digit in some_list]
    return some_list