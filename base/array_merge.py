


class Array:
    """
    实现两个有序数组合并为一个有序数组,简单思路：保持一个有序数组，然后倒序另一个有序数组遍历添加进来。
    """

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def add(self, elem):
        """
        添加元素到数组, 这应该是一个自动扩容的数组
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
        for i in range(self._size - 1, -1, -1):  # 倒序遍历size-1到0
            if elem < self._data[i]:
                self._data[i + 1] = self._data[i]  # 后移比当前大的数
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
        """两个有序数组合并优化，没有数据搬移操作，时间复杂度：O(n)
        
        Arguments:
            arr {[Array]} -- [Array类实例]
        """
        if len(arr) == 0:
            print("数组长度不能为0")
            return

        if type(arr) != Array:
            print("传入的数组不是Array类型")
            return

        new_size = self._size + len(arr)

        temp_arr = Array(new_size)
        temp_index = 0
        left_arr_index = 0
        right_arr_index = 0
        while temp_index < new_size:
            while temp_index < new_size:

                # 边界条件检查,左边数组已经添加完毕，直接把右边剩余添加进来
                if left_arr_index == self._size:
                    for i in range(right_arr_index, arr._size):
                        temp_index, right_arr_index = self._add_data(
                            temp_index, right_arr_index, temp_arr, arr)
                    break

                # 边界条件检查,右边数组已经添加完毕，直接把左边剩余边添加进来
                if right_arr_index == arr._size:
                    for i in range(left_arr_index, self._size):
                        temp_index, left_arr_index  = self._add_data(
                            temp_index, left_arr_index, temp_arr, self)
                    break

                if self._data[left_arr_index] < arr._data[right_arr_index]:
                    temp_index, left_arr_index = self._add_data(temp_index, left_arr_index, temp_arr, self)
                    break

                if self._data[left_arr_index] == arr._data[right_arr_index]:
                    temp_index, left_arr_index= self._add_data(temp_index, left_arr_index, temp_arr, self)
                    temp_index, right_arr_index = self._add_data(temp_index, right_arr_index, temp_arr, arr)
                    break
                
                if self._data[left_arr_index] > arr._data[right_arr_index]:
                    temp_index, right_arr_index = self._add_data(temp_index, right_arr_index, temp_arr, arr)
                    break

        self._data = temp_arr._data
        self._capacity = new_size
        self._size = new_size

    def __len__(self):
        return self._size

    def _add_data(self, temp_index, index, temp_arr, arr):
        temp_arr._data[temp_index] = arr._data[index]
        index += 1
        temp_index += 1
        return temp_index, index

arr = Array(10)
for i in range(10, 0, -1):
    arr.add(i)
# arr.print()

arr1 = Array(20)
for i in range(20, 10, -1):
    arr1.add(i)

# arr.merge(arr1)
arr.merge_insert(arr1)
arr.print()

# TODO：是否有优化地方？ 添加元素时，查找适合的插入点，这个是有序数据，二分发在平均意义上是不是时间复杂度更低。
#   TypeError: 'Array' object is not subscriptable
#   __len__
# 合并思路优化：遍历两个数组，选出最小的值，放入新的数组，知道两个数组没有元素就退出

# for i in range(1, 1, -1):
#     print(i)
# help(range)
