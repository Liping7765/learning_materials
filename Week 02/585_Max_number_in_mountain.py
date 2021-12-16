# Binary Search 
# no repeated numbers in the array
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here

        left, right = 0, len(nums) - 1

        while left + 1 < right :

            middle = (left + right) // 2

            if nums[middle] < nums[middle + 1] :
                left = middle

            else:
                right = middle 

        #return max(nums[left], nums[right])
        if nums[left] > nums[right] :
            return nums[left]

        else:
            return nums[right]

    

            


