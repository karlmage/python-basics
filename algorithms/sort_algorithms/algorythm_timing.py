# Source: https://realpython.com/sorting-algorithms-python/

from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array_length = 10000):

    array = [randint(0, 1000) for i in range(array_length)]

    stmt = lambda: algorithm(array)

    times = repeat(stmt = stmt, number = 10)

    print(f"Algorithm: {algorithm.__name__}. Minimum execution time: {min(times)}")

if __name__ == "__main__":
    from algorithms.sort_algorithms.bubble_sort.bubble_sort import bubble_sort
    from algorithms.sort_algorithms.insertion_sort.insertion_sort import insertion_sort
    from algorithms.sort_algorithms.merge_sort.merge_sort import merge_sort
    from algorithms.sort_algorithms.quick_sort.quick_sort import quick_sort
    from algorithms.sort_algorithms.tim_sort.tim_sort import tim_sort

    run_sorting_algorithm(bubble_sort)
    run_sorting_algorithm(insertion_sort)
    run_sorting_algorithm(merge_sort)
    run_sorting_algorithm(quick_sort)
    run_sorting_algorithm(tim_sort)