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


public class Solution {
    /**
     * @param nums a list of integer
     * @return an integer, maximum coins
     */
    public int maxCoins(int[] AA) {
        // Write your code here
        int n = AA.length;
        if (n == 0) {
            return 0;
        }
        
        int i, j, k, len;
        int[] A = new int[n + 2];
        A[0] = A[n + 1] = 1;
        for (i = 1; i <= n; ++i) {
            A[i] = AA[i - 1];
        }
        
        n += 2;
        int[][] f = new int[n][n];
        for (i = 0; i < n - 1; ++i) {
            f[i][i+1] = 0; // balloon balloon
        }
        
        for (len = 3; len <= n; ++len) {
            for (i = 0; i <= n - len; ++i) {
                j = i + len - 1;
                f[i][j] = 0;
                for (k = i + 1; k < j; ++k) {
                    f[i][j] = Math.max(f[i][j], f[i][k] + f[k][j] + A[i] * A[k] * A[j]);
                }
            }
        }
        
        return f[0][n - 1];
    }
}

