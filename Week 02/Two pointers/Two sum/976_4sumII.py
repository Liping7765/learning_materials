#Two sum 
class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        # Write your code here
        a = {}
        for a in A:
            for b in B:
                a[a + b] = a.get(a + b, 0) + 1

        count = 0
        for c in C:
            for d in D:
                count += a.get(-c - d, 0)

        return count 


""" 
review session:

divide and conquer 

"""