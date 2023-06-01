# 定义一个链表类

class ListNode:
    # 定义一个值和指针属性
    def __init__(self, val):
        self.val = val
        self.next = None


# 将列表转化为链表

def list_to_linked_list(list):
    # 1. 创建一个没有存放任何内容的哑节点, 用一个固定的指针dummy指向这个节点
    dummy = ListNode(0)
    # 2. 用一个可移动得指针p指向这个节点
    p = dummy
    # 3. 开始遍历列表, 将列表中的每一个元素作为值创造节点实例
    for i in list:
        # 4. 创建节点. 连接到p指向的节点之后
        p.next = ListNode(i)
        # 5. 更新指针, 将可移动的指针p指向最新的新加入的节点
        p = p.next
    # 6. 遍历完成之后, 返回首节点的位置
    return dummy.next




















