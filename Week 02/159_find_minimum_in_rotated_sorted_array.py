#binary search 

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here

        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        last = nums[right]

        while left + 1 < right:

            middle = (left + right) // 2

            if nums[middle] > last :
                left = middle 

            else:
                right = middle 

            
        return min(nums[left], nums[right])


"""
follow up question:
1. what if you need to look for value k in this array?
2. what if you can only binary search it once ?

"""

