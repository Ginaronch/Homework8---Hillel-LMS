def add_one(some_list):
    string = ''
    some_list = (string.join(str(element) for element in some_list))
    some_list = str(int(some_list) + 1)
    some_list = [int(num) for num in some_list]
    return some_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]
print("ОК")