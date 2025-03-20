def linear_search(array, key):
    """
    :param array: list of data
    :param key: value which needs to be checked, whether it exists in list or not
    :return: the index of the element
    """
    array.append(key)
    i = 0
    while array[i] != key:
        i += 1
    return i if i < len(array) - 1 else -1


L = [3, 24, 56, 17, 99, 32, 41, 0]
N = 55
print(linear_search(L, N))