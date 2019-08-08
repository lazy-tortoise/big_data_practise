# 实现一个大小固定的有序数组，支持动态增删改操作
class Array:

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None]*capacity

    def add(self, elem):
        """
        添加元素到数组
        :param elem: 元素
        """
        index = 0
        # 找到被插入的位置，并赋值给index
        for i in range(self._size):
            if elem < self._data[i]:
                break
            else:
                index = i

        # 把index+1的元素向后移动， 如数组长度等于数组初始化长度，最后一位数据将被移除
        for i in range(self._size-1, index-1, -1):
            if i == self._capacity-1:
                continue
            self._data[i+1] = self._data[i] 
        self._data[index] = elem
        if self._size < self._capacity:
            self._size += 1

    def delete(self, index):
        """
        删除元素
        """
        if index < 0 or index > self._size:
            print("index不合法")
            return
        for i in range(index+1, self._size, 1):
            self._data[i-1] = self._data[i]
            self._data[i] = [None]

        self._size = self._size - 1

    def print(self):
        for i in range(self._size):
            print(self._data[i])


arr = Array(10)
arr.add(20)
arr.add(19)
arr.add(15)
arr.add(13)
arr.add(10)
arr.add(7)
arr.add(6)
arr.add(5)
arr.add(4)
arr.add(3)
arr.add(2)
arr.add(1)
arr.add(0)
arr.delete(7)
arr.delete(9)
arr.print()

# 收获一: range的step=1，时候，stop，只会执行到stop-1 验证代码如下：
for i in range(1, 3, 1):
    print(i)

# 思考：是否有优化地方？ 添加元素时，查找适合的插入点，这个是有序数据，二分发在平均意义上是不是时间复杂度更低。
