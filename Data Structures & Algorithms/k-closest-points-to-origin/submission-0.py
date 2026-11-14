from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-1, [])] + [(x * x + y * y, [x, y]) for x, y in points]
        self.heapify(heap)
        return [self.pop(heap)[1] for _ in range(k)]

    def sift_down(self, arr, i):
        while 2 * i < len(arr):
            node = arr[i]
            if 2 * i + 1 < len(arr):
                if node[0] > arr[2 * i + 1][0] and arr[2 * i + 1][0] < arr[2 * i][0]:
                    arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                    i = 2 * i + 1
                elif node[0] > arr[2 * i][0]:
                    arr[i], arr[2 * i] = arr[2 * i], arr[i]
                    i = 2 * i
                else:
                    break
            else:
                if node[0] > arr[2 * i][0]:
                    arr[i], arr[2 * i] = arr[2 * i], arr[i]
                    i = 2 * i
                else:
                    break

    def heapify(self, arr):
        j = (len(arr) - 1) // 2
        while j >= 1:
            self.sift_down(arr, j)
            j -= 1

    def pop(self, arr):
        if len(arr) <= 1:
            return None
        arr[1], arr[-1] = arr[-1], arr[1]
        value = arr.pop()
        self.sift_down(arr, 1)
        return value