import math
import statistics
from heapq import heappush, heappop, heapify

import numpy as np


class MedianFinderSimple(object):
    def __init__(self):
        self.xs = []

    def add_num(self, new_x):
        self.xs.append(new_x)

    def median(self):
        return statistics.median(self.xs)


class MedianFinder(object):
    def __init__(self):
        self.xs = []

    def add_num(self, new_x):
        n = len(self.xs)
        i = 0
        while i < n and new_x > self.xs[i]:
            i += 1
        self.xs.insert(i, new_x)

    def median(self):
        n = len(self.xs)
        i = n // 2
        if n % 2 == 0:
            return 0.5 * (self.xs[i - 1] + self.xs[i])
        else:
            return self.xs[i]


def repair_down(xs, i):
    n = len(xs)
    i_left = i * 2 + 1
    i_right = i * 2 + 2
    i_max = i
    if i_left < n and xs[i_left] > xs[i_max]:
        i_max = i_left
    if i_right < n and xs[i_right] > xs[i_max]:
        i_max = i_right

    if i_max != i:
        xs[i], xs[i_max] = xs[i_max], xs[i]
        repair_down(xs, i_max)


def repair_up(xs, i):
    i_parent = (i - 1) // 2
    if xs[i_parent] < xs[i]:
        xs[i_parent], xs[i] = xs[i], xs[i_parent]

    if i_parent > 0:
        repair_up(xs, i_parent)


def heap_add(xs, x):
    xs.append(x)
    repair_up(xs, len(xs) - 1)


def heap_remove(xs):
    n = len(xs)
    xs[0], xs[n - 1] = xs[n - 1], xs[0]
    xs.pop()
    repair_down(xs, 0)


class MedianFinderHeap(object):
    def __init__(self):
        self.left = []
        self.right = []

    def add_num(self, new_x):
        if len(self.left) == 0:
            self.left.append(new_x)
            # print(f'L={self.left}')
            # print(f'R={self.right}')
            return
        if len(self.right) == 0:
            if self.left[0] <= new_x:
                self.right.append(-new_x)
            else:
                self.right.append(-self.left[0])
                self.left[0] = new_x
            return

        if new_x <= self.left[0]:
            new_x, self.left[0] = self.left[0], new_x
            repair_down(self.left, 0)
        elif new_x >= -self.right[0]:
            new_x, self.right[0] = -self.right[0], -new_x
            repair_down(self.right, 0)

        if len(self.left) <= len(self.right):
            heap_add(self.left, new_x)
        else:
            heap_add(self.right, -new_x)

        # print(f'L={self.left}')
        # print(f'R={self.right}')

    def median(self):
        if len(self.left) > len(self.right):
            return self.left[0]
        else:
            return 0.5 * (self.left[0] - self.right[0])


class MedianFinderHeapGG(object):
    def __init__(self):
        self.minHeap = []
        heapify(self.minHeap)
        self.maxHeap = []
        heapify(self.maxHeap)

    def add_num(self, num):
        heappush(self.maxHeap, -num)  ### Pushing negative element to obtain a minHeap for
        heappush(self.minHeap, -heappop(self.maxHeap))  ### the negative counterpart

        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

        # print(f'maxHeap={self.maxHeap}')
        # print(f'minHeap={self.minHeap}')

    def median(self):
        if len(self.minHeap) != len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2


# xs = []
# heap_add(xs, 4)
# heap_add(xs, 10)
# heap_add(xs, 3)
# heap_add(xs, 5)
# heap_add(xs, 1)
# print(xs)
#
# xs_ = [4, 10, 3, 5, 1]
# heapify(xs_, 3)
# print(xs)

finder0 = MedianFinderSimple()
finder1 = MedianFinder()
finder2 = MedianFinderHeap()
finder3 = MedianFinderHeapGG()

for i in np.random.randint(10, size=100):  # np.random.randint(10, size=10)
    finder0.add_num(i)
    finder1.add_num(i)
    finder2.add_num(i)
    finder3.add_num(i)
    print(finder0.median())
    print(finder1.median())
    print(finder2.median())
    print(finder3.median())
    if finder2.median() != finder3.median():
        print('Error')
