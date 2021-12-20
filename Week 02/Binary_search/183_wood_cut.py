class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here

        if not L:
            return 0

        #set a maximum guess of the answers
        max_length = sum(L) // k
        if not max_length:
            return 0

        #binary search the sorted array -> answer set -> range(0,max_length) 
        # find the greatest value that its max woodcuts is greater or equal to k 

        left, right = 0, max_length

        while left + 1 < right:

            middle = (left + right) // 2
            max_woodcuts = self.find_max_woodcuts(L, middle)

            if max_woodcuts >= k:
                left = middle

            else:
                right = middle 
            
        return right if self.find_max_woodcuts(L, right) >= k else left
    
    def find_max_woodcuts(self, L, length):
        return sum(wood//length for wood in L)


"""
errors:

1. After while loop, right could be 0. 
The reason is due to max_length could be ZERO after the whole sum division.

2. sum(wood//length for wood in L)

"sum([wood//length for wood in L])" would double the rumtime because it needs to create the list first,
and them sum them up 

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(L, mid) >= k:
                start = mid
            else:
                end = mid
                
        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
            
        return 0
        
    def get_pieces(self, L, length):
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces

"""
