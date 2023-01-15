import time
import random
from random import randint
import array as arr
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    start = time.time()

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    end = time.time()

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    print(f"Algorithm: {algorithm}. Execution time: {end - start}")


def insertion_sort(array):
  for i in range(1, len(array)):
    a = i 
    while a > 0 and array[a]<array[a-1]:
        array[a-1],array[a]=array[a],array[a-1]
        a -= 1
  return array

print(insertion_sort(arr.array('i', [random.randint(i,60) for i in range(15)])))

if __name__ == "__main__":
    array = [randint(i, 60) for i in range(15)]

    run_sorting_algorithm(algorithm="sorted", array=array)
    run_sorting_algorithm(algorithm="insertion_sort", array=array)
