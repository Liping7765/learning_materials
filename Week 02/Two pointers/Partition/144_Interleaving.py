# partition
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here

        #partition the array into two parts 

        left, right = 0, len(A) - 1

        while left <= right:

            if A[left] < 0:
                left += 1
                continue 

            if A[right] > 0:
                right -= 1
                continue 

            A[left], A[right] = A[right], A[left]

            left += 1
            right -= 1

        if not (len(A) // 2) % 2 :
            left += 1
            right -= 1

        while left <= len(A) - 1 and right >= 0:

            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2

        return A


"""
see solution for more details of interleaving part
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1
        
        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)
            
    def partition(self, A, start_positive):
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
    
    def interleave(self, A, has_same_length):
        left, right = 1, len(A) - 1
        if has_same_length:
            right = len(A) - 2
            
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2


review session

scenario 1 : if len(A) == len(B) or even numbers, then l = 1, r = -2, leaping two 
DEMO:
[AAABBB] -> [ABABAB]
  l  r

scenario 2 : if len(A) > len(B) or odd numbers, then l = 1, r = -1, leaping two 
[AAAABBB] -> [AbAABBa] -> [AbAbaBa]
  l    r               

"""
