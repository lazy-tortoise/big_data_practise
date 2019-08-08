class Array:
    """实现一个支持动态扩容的数组
    数组是一种线性表，他是一组连续内存空间,支持随机（索引）访问，存储相同类型数据。
    查询时间复杂度是O(1)
    删除插入元素时间复杂度是O(n)
    """

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0  # 数组已使用的大小
        self._data = [None]*self._capacity  # 初始化元素

    def add(self, index, elem):
        """添加元素到数组
        :param index: 索引
        :param elem: 元素
        """

        # 判断index是否超出标准
        if index < 0 or index > self._size:
            print("index超出范围")
            return

        if self._size == self._capacity:
            self._resize(self._capacity*2)

        # 搬移数据到index之后
        for i in range(self._size-1, index-1, -1):
            self._data[i+1] = self._data[i]

        # 然后将elem插入到index
        self._data[index] = elem
        self._size = self._size + 1

    def _resize(self, new_capacity):
        new_arr = Array(new_capacity)
        for i in range(self._size):
            new_arr.add(i, self._data[i])

        self._capacity = new_capacity
        self._data = new_arr._data

    def print(self):
        for i in range(self._size):
            print(self._data[i])


arr = Array(10)
for i in range(10):
    arr.add(i, i)
arr.add(10, 11)
arr.add(11, 12)
arr.add(12, 13)
arr.print()
arr.print()

"""
收获一：help(range),第三个参数是step,为负数时，就可以从大到小进行循环了。
"""
