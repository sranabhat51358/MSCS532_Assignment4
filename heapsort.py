"""
Implements Heapsort using a Max-Heap.
Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def build_max_heap(self):
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def sort(self):
        n = len(self.arr)
        self.build_max_heap()

        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heapify(i, 0)

        return self.arr


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Sorted:", HeapSort(data).sort())
