def heapify(numbers: list[int], total_count: int, root_index: int, sign: int):
    """
    :param numbers: the array of numbers that needs to be sorted
    :param total_count: the total number of elements present in the array
    :param root_index: the index of the node under consideration
    :param sign: 1 for ascending order, -1 for reverse order
    :return: nothing, as it modifies the original array
    :explanation:
        consider an example array [1, 2, 3, 4, 5, 6, 7, 8, 9] and convert it into a binary tree
                         1
                       /  \
                      2    3
                     / \  / \
                    4   56   7
                   / \
                  8   9
        root_index start from total_count // 2 - 1 and moves up till zero
        for e.g. in our example 9 // 2 - 1 = 3
        so our node value is 4 (numbers[3]) and child values are 8 and 9 (based on 2*i+1 and 2*i+2 for indices)
        and it moves down the tree, till no child nodes are found
    """
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
    """
    :param numbers: list of unordered numbers
    :param reverse: determines ascending or descending. ascending, by default.
    :return:
    """
    sign = -1 if reverse else 1
    total_count = len(numbers)
    # This step ensures that a max heap is created out of the given list
    # It means the largest element will be bubbled up to the top
    for root_index in range(total_count // 2 - 1, -1, -1):
        heapify(numbers, total_count, root_index, sign)
    # Once we have the largest element on the top, swap ot with the bottom most element
    # Now ignore the last element and re-heap, so that the next largest will be at the top
    # Swap it with the second last position and continue this process till the list is sorted
    for index in range(total_count - 1, -1, -1):
        numbers[index], numbers[0] = numbers[0], numbers[index]
        heapify(numbers, index, 0, sign)
    return numbers


L = [32, 24, 10, 55, 89, 13, 23, 24]
print(heap_sort(L))
print(heap_sort(L, True))


