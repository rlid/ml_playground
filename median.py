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


def heapify(xs, i):
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
        heapify(xs, i_max)


def heap_add(xs, x):
    i_parent = (len(xs) - 1) // 2
    xs.append(x)
    heapify(xs, i_parent)


def heap_remove(xs):
    n = len(xs)
    xs[0], xs[n - 1] = xs[n - 1], xs[0]
    xs.pop()
    heapify(xs, 0)


class MedianFinderHeap(object):
    def __init__(self):
        self.left = []
        self.right = []

    def add_num(self, new_x):
        if len(self.right) > 0:
            if new_x < self.left[0]:
                new_x, self.left[0] = self.left[0], new_x
                heapify(self.left, 0)
            else:
                new_x, self.right[0] = -self.right[0], -new_x
                heapify(self.right, 0)

        if len(self.left) <= len(self.right):
            heap_add(self.left, new_x)
        else:
            heap_add(self.right, -new_x)

        print(f'L={self.left}')
        print(f'R={self.right}')

    def median(self):
        if len(self.left) > len(self.right):
            return self.left[0]
        else:
            return 0.5 * (self.left[0] - self.right[0])


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

finder = MedianFinderHeap()
finder.add_num(1)
finder.add_num(2)
print(finder.median())
finder.add_num(3)
print(finder.median())
