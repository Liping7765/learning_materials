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
"""
