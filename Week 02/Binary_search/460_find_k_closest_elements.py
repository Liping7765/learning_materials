#binary search 

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here

        #binary search its postion of insertion 

        left, right = 0, len(A) - 1

        while left + 1 < right :

            middle = (left + right) // 2

            if A[middle] <= target:

                left = middle 

            if A[middle] > target:

                right = middle



        #use two pointers to rank the results

        results = []

        for _ in range(k):

            if abs(A[left] - target) <= abs(A[right] - target) :
                results.append(A[left])
                left -= 1

            else:
                results.append(A[right])
                right = (right + 1) % len(A)

        return results


    
"""
review session:

1. "A[middle] <= target" ->  [k - 1, k + 1]  or [k, k + 1]
2. "A[middle] >= target" ->  [k - 1, k + 1]  or [k - 1, k]

"""



