# Source: https://realpython.com/sorting-algorithms-python/

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array

if __name__ == "__main__":
    from algorithms.sort_algorithms.algorythm_timing import run_sorting_algorithm

    run_sorting_algorithm(bubble_sort)
