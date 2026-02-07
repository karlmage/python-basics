# Source: https://realpython.com/sorting-algorithms-python/

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1

        while j >= left and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def tim_sort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), n - 1)

            merged_array = merge(array[start:midpoint + 1],
                                 array[midpoint + 1:end + 1])

            array[start: start + len(merged_array)] = merged_array

        size *= 2

if __name__ == '__main__':
    from algorithms.sort_algorithms.algorythm_timing import run_sorting_algorithm

    run_sorting_algorithm(tim_sort)