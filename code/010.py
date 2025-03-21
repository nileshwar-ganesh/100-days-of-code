def binary_search(array, key):
    return search_procedure(array, key,0, len(array))

def search_procedure(array, key, left, right):
    if left < right:
        mid = (left + right) // 2
        if array[mid] == key:
            return "The item exists"
        elif array[mid] > key:
            return search_procedure(array, key, left, mid)
        elif array[mid] < key:
            return search_procedure(array, key, mid + 1, right)
    else:
        return "The item does not exists"


"""
Using Heap Sort to sort the given list before binary search
For detailed explanation on how heap sort works, check Day 006 implementation
"""
def heapify(numbers: list[int], total_count: int, root_index: int, sign: int):
    index_largest_value = root_index
    index_left_child = 2 * root_index + 1
    index_right_child = 2 * root_index + 2
    if index_left_child < total_count and sign * numbers[index_left_child] > sign * numbers[index_largest_value]:
        index_largest_value = index_left_child
    if index_right_child < total_count and sign * numbers[index_right_child] > sign * numbers[index_largest_value]:
        index_largest_value = index_right_child
    if index_largest_value != root_index:
        numbers[index_largest_value], numbers[root_index] = numbers[root_index], numbers[index_largest_value]
        heapify(numbers, total_count , index_largest_value, sign)

def heap_sort(numbers: list[int], reverse: bool=False) -> list[int]:
    sign = -1 if reverse else 1
    total_count = len(numbers)
    for root_index in range(total_count // 2 - 1, -1, -1):
        heapify(numbers, total_count, root_index, sign)
    for index in range(total_count - 1, -1, -1):
        numbers[index], numbers[0] = numbers[0], numbers[index]
        heapify(numbers, index, 0, sign)
    return numbers


L = [32, 24, 10, 55, 89, 13, 23, 24]
L = heap_sort(L)
print(binary_search(L, 33))


