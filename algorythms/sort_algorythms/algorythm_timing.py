# Source: https://realpython.com/sorting-algorithms-python/

from random import randint
from timeit import repeat

def run_sorting_algorythm(algorythm, array_length = 1000):
    setup_code = f"from __main__ import {algorythm}" \
        if algorythm != "sorted" else ""

    stmt = f"{algorythm}({[[randint(0, 100) for i in range(array_length)]]})"

    times = repeat(setup = setup_code, stmt = stmt, number = 10)

    print(f"Algorithm: {algorythm}. Minimum execution time: {min(times)}")

if __name__ == "__main__":
    run_sorting_algorythm(algorythm = "sorted")