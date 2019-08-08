# 实现两个有序数组合并为一个有序数组


class Array:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def add(self, elem):
        """
        添加元素到数组, 这应该是一个自动扩容的数组
        :param elem: 元素
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        # 对边界条件进行设置
        if self._size == 0:
            self._data[0] = elem
            self._size += 1
            return

            # # 找到被插入的位置，并赋值给index
            # for i in range(self._size):
            #     if elem < self._data[i]:
            #         break
            #     else:
            #         index = i

            # # 把index+1的元素向后移动
            # for i in range(self._size-1, index+1, -1):
            #     self._data[i+1] = self._data[i]

        # 倒序遍历数组，移动后面的元素，直到找到插入位置
        index = self._size - 1
        for i in range(self._size - 1, -1, -1):
            if elem < self._data[i]:
                self._data[i + 1] = self._data[i]
                index = i
            else:
                break

        self._data[index] = elem
        self._size += 1

    def _resize(self, new_capacity):
        new_arr = Array(new_capacity)
        for i in range(self._size):
            new_arr.add(self._data[i])

        self._capacity = new_capacity
        self._data = new_arr._data

    def delete(self, index):
        """
        删除元素
        """
        if index < 0 or index > self._size:
            print("index不合法")
            return
        for i in range(index + 1, self._size, 1):
            self._data[i - 1] = self._data[i]
            self._data[i] = [None]

        self._size = self._size - 1

    def print(self):
        for i in range(self._size):
            print(self._data[i])

    def merge(self, arr):
        if len(arr) == 0:
            print("数组长度不能为0")
            return

        if type(arr) != Array:
            print("传入的数组不是Array类型")
            return

        self._resize(self._size + len(arr))

        for i in range(arr._size):
            self.add(arr._data[i])

    def merge_insert(self, arr):
        pass

    def __len__(self):
        return self._size


arr = Array(10)
for i in range(10, 0, -1):
    arr.add(i)
# arr.print()

arr1 = Array(20)
for i in range(20, 10, -1):
    arr1.add(i)

arr.merge(arr1)
arr.print()

# 思考：是否有优化地方？ 添加元素时，查找适合的插入点，这个是有序数据，二分发在平均意义上是不是时间复杂度更低。
#   TypeError: 'Array' object is not subscriptable
#   __len__
# 合并思路优化：遍历两个数组，选出最小的值，放入新的数组，知道两个数组没有元素就退出

# for i in range(1, 1, -1):
#     print(i)
# help(range)