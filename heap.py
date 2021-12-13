import math


class Heap(object):

    def __init__(self, nums):
        self.cache = nums or []
        self._heapify()

    def __len__(self):
        return len(self.cache)

    def __bool__(self):
        return len(self.cache) > 0

    def __repr__(self):
        return f'heap({self.cache})'

    @property
    def size(self):
        return len(self.cache) - 1

    @property
    def largest(self):
        if not self.cache:
            raise Exception('Empty heap')
        return self.cache[0]

    def show(self):
        # 调用这个函数绘制一颗二叉树出来,DEBUG用
        height = int(math.log2(len(self))) + 1
        for i in range(height):
            width = 2 ** (height - i) - 2
            print(' ' * width, end='')
            blank = ' ' * (width * 2 + 2)
            print(
                blank.join(['{: >2d}'.format(num) for num in self.cache[2 ** i - 1:min(2 ** (i + 1) - 1, len(self))]]))
            print()

    def _swap(self, i, j):
        # 这个方法交换二叉树的两个节点
        self.cache[i], self.cache[j] = self.cache[j], self.cache[i]

    def push(self, num):
        self.cache.append(num)
        # self.size
        self._siftup(self.size)

    def _siftup(self, i):
        while i > 0:
            parent = (i - 1) >> 1
            if self.cache[i] <= self.cache[parent]:
                break
            self._swap(i, parent)
            i = parent

    def pop(self):
        largest = self.largest
        self._swap(0, len(self) - 1)
        self.cache.pop()
        self._siftdown(0)
        return largest

    def _siftdown(self, i):
        while i * 2 + 1 < len(self):
            smaller = i
            if self.cache[i * 2 + 1] > self.cache[smaller]:
                smaller = i * 2 + 1
            if i * 2 + 2 < len(self) and self.cache[i * 2 + 2] > self.cache[smaller]:
                smaller = i * 2 + 2
            if smaller == i:
                return
            self._swap(i, smaller)
            i = smaller

    def _heapify(self):
        for i in reversed(range(len(self) // 2)):
            self._siftdown(i)

    def top_k(self, k):
        return [self.pop() for _ in range(k)]



if __name__ == '__main__':
    import random

    nums = list(range(20))
    random.shuffle(nums)
    heap = Heap(nums[:])
    heap.show()

    print(heap.top_k(5))

    # print(heap.top_k(2))
    # heap.push(19)
    # print('插入19')
    # heap.show()
    #
    # heap.pop()
    # print('弹出堆顶元素')
    # heap.show()

    # for _ in range(100):
    #     num = random.randrange(100)
    #     nums.append(num)
    #     heap.push(num)
    #     assert max(nums) == heap.largest
    #     nums.remove(heap.pop())
    #
    # print('所有测试通过!!!')