class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        len_L = len(L)
        if len_L == 0:
            return 0
        max_L = 0
        for i in range(len_L):
            max_L = max(max_L,L[i])
        left,right = 0,max_L
        def check(mid):
            cou = 0
            #计算当前长度下能分成几段
            for i in range(len_L):
                cou += (int)(L[i] / mid)
            #如果还能分更长的，返回true
            if cou >= k:
                return True
            #如果不能分更长的，返回false
            return False
        while left + 1 < right:
            mid = (int)(left + (right - left) / 2)
            if check(mid):#如果还能分更长的，则往[mid,right]走
                left = mid
            else:#如果不能分更长的，则往[left,mid]走
                right = mid
        if check(right):
            return right
        return left