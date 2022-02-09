"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param node: a list node in the list
    @param x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        # 边界
        cur_node = ListNode(x)
        if node == None: return cur_node

        # 遍历 寻找插入点 终止条件是回到起点
        start = node
        node = node.next
        while node != start:
            # 进行比较
            if node.val <= x and node.next.val >= x:
                return self.ins_node(cur_node, node)
            node = node.next
        
        # x比链表值都大/小/等
        while node.val < node.next.val:
            node = node.next
        return self.ins_node(cur_node, node)


    def ins_node(self, cur_node, node):
        cur_node.next = node.next
        node.next = cur_node
        return cur_node