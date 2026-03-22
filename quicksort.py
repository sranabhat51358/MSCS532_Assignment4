"""
Recursive Quicksort implementation.
Average: O(n log n)
Worst: O(n^2)
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    print("Sorted:", quicksort([10, 7, 8, 9, 1, 5]))
