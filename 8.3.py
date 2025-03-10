def find_unique_value(some_list):
    for element in some_list:
        if some_list.count(element) == 1:
            return element
        elif not some_list:
            return None
assert find_unique_value([1, 2, 1, 1]) == 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5
assert find_unique_value([]) is None
print("ОК")