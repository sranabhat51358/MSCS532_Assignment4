"""
Compare sorting algorithms across:
- Random
- Sorted
- Reverse datasets
"""

import random
import time
from heapsort import HeapSort
from quicksort import quicksort
from mergesort import merge_sort


def generate_random(size):
    return [random.randint(1, 100000) for _ in range(size)]


def generate_sorted(size):
    return list(range(size))


def generate_reverse(size):
    return list(range(size, 0, -1))


def measure_time(func, data):
    start = time.time()
    func(data)
    return time.time() - start


def run_experiment():
    sizes = [1000, 5000, 10000]

    datasets = {
        "Random": generate_random,
        "Sorted": generate_sorted,
        "Reverse": generate_reverse
    }

    for name, generator in datasets.items():
        print(f"\n===== {name} Dataset =====")

        for size in sizes:
            data = generator(size)

            heap_time = measure_time(lambda x: HeapSort(x).sort(), data.copy())
            quick_time = measure_time(quicksort, data.copy())
            merge_time = measure_time(merge_sort, data.copy())
            python_time = measure_time(lambda x: x.sort(), data.copy())

            print(f"\nSize: {size}")
            print(f"Heapsort:    {heap_time:.6f}s")
            print(f"Quicksort:   {quick_time:.6f}s")
            print(f"Merge Sort:  {merge_time:.6f}s")
            print(f"Python Sort: {python_time:.6f}s")


if __name__ == "__main__":
    run_experiment()
