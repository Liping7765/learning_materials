#binary search 

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here

        #binary search its middle to identify if the solution on its left or right

        left, right = 0, len(A) - 1

        while left + 1 < right :

            middle = (left + right) // 2

            if A[middle] > A[middle + 1]:
                right = middle

            else:
                left = middle


        return left if A[left] > A[right] else right


"""
二分法

每次取中间元素，如果大于左右，则这就是peek。 否则取大的一边，两个都大，可以随便取一边。最终会找到peek。

正确性证明
1. A0 < A1 && An-2 > An-1 所以一定存在一个peek元素。 
2. 二分时，选择大的一边, 则留下的部分仍然满足1 的条件，即最两边的元素都小于相邻的元素。所以仍然必然存在peek。 
3. 二分至区间足够小，长度为3, 则中间元素就是peek。

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        start, end = 1, len(A) - 2
        while start + 1 <  end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                return mid

        if A[start] < A[end]:
            return end
        else:
            return start

"""
