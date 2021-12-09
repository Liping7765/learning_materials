#quicksort 

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here

        #validate input 
        if not A or len(A)==1:
            return A

        self.quicksort(A,0,len(A)-1)

        return A

    def quicksort(self, A, start, end):

        #validate input 
        if start >= end:
            return

        #initialize two pointers left, right, and pivot 
        left, right = start, end 
        #注意点3
        pivot = A[(left + right) // 2]
        #注意点1
        while(left <= right):
            #注意点2
            if A[left] < pivot:
                left += 1
                continue 

            if A[right] > pivot:
                right -= 1
                continue 

            temp = A[left]
            A[left] = A[right]
            A[right] = temp
            left += 1
            right -= 1

        self.quicksort(A, start, right)
        self.quicksort(A, left, end)

"""

review session:
1. "while(left <= right)" to avoid stack overflow eg [1,2] 
2.  given that a[left] <= pivot, we will move forward to next index which may cause unevenly long array.
    In this case, time compexity will be O(n^2). Among left and right, which side gets executed first will
    have more pivot numbers on its side. eg [1,1,1,1,1,2]

3. [x,x,x,x,x,x+1]  should better be split into [x,x,x] and [x,x,x+1]
    condition "a[left] <= pivot" will cause situation like [x,x,x,x,x] and [x+1]
"""


# mergsort

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here

        if not A or len(A) == 1:
            return A

        temp = [0 for _ in A]
        self.mergesort(A,0,len(A)-1,temp)

        return A

    
    def mergesort(self, A, start, end, temp):

        #check input 
        if start >= end:
            return 

        #split array into two and merge sort them seperately
        middle = (start + end)// 2

        self.mergesort(A, start, middle, temp)
        self.mergesort(A, middle+1, end, temp)
        
        #merge two sorted array 
        self.merge(A, start, middle, end, temp)

        return 

    def merge(self, A, start, middle, end, temp):

        left, right = start, middle + 1

        for i in range(start, end+1):
            if left > middle:
                temp[i] = A[right]
                right += 1
                continue

            if right > end:
                temp[i] = A[left]
                left += 1
                continue

            if A[left] <= A[right]:
                temp[i] = A[left]
                left += 1
                continue 

            temp[i] = A[right]
            right += 1

        for i in range(start, end + 1):
            A[i] = temp[i]

        return 


"""
review session
1. we need extra space for swapping the position of the array so we need to create a temp array 
   same rules apply when merging two linked lists.
   the reasoning is that the number will overide the list in some of the cases given there's limited spots
2. good thing is that i coud figure out how to split the array myself.
   This case could avoid stack overflow.
eg. [x,x] 
    middle = 0 
    left = 0 right = 1
    (0,0) (1,1)

"""
