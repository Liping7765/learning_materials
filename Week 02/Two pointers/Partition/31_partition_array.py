#partition 
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums :
            return 0

        left, right = 0, len(nums) -1 


        while left <= right:

            if nums[left] < k:
                left += 1
                continue 

            if nums[right] >= k:
                right -= 1
                continue 

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return left 




"""
Review session:

1. why "left <= right" ?

if "left < right", left point might stop at the right pointer, and you could not tell if this number is 
the first of the right partition or the last of the left parttion. 

in order to avoid troubles, using "left <= right" will ensure left starts at the first of the right partition.

2. the features of partition 
    a. not stable swap -> cannot remain original order 
    b. in-place 
    c. time complexity of O(n)
    d. while left <= right -> left <= target / right > target 
    
"""