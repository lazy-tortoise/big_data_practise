# 不知道单链表长度,知道头节点和尾节点，求中间节点位置
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next    


n1 = Node('n1', None)
n2 = Node('n2', n1)
n3 = Node('n3', n2)
n4 = Node('n4', n3)
n5 = Node('n5', n4)
n6 = Node('n6', n5)
n7 = Node('n7', n6)
n8 = Node('n8', n7)
n9 = Node('n9', n8)
n10 = Node('n10', n9)

p1 = n10  # 慢指针
p2 = n10  # 快指针
while p2.next is not None and p2.next.next is not None:
    p1 = p1.next
    p2 = p2.next.next
print(p1.data)
if p2.next is not None and p2.next.next is None:
    print(p1.next.data)