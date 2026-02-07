# Source: https://realpython.com/sorting-algorithms-python/

def insertion_sort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

if __name__ == "__main__":
    from algorithms.sort_algorithms.algorythm_timing import run_sorting_algorithm

    run_sorting_algorithm(insertion_sort)