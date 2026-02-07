# Source: https://realpython.com/sorting-algorithms-python/

from random import randint

def quick_sort(array):
    if len(array) < 2:
        return array

    low = same = high = []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)

if __name__ == '__main__':
    from algorythms.sort_algorythms.algorythm_timing import run_sorting_algorythm
    run_sorting_algorythm("quick_sort")