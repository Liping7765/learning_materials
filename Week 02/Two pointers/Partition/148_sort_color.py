class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here

        left, index, right = 0, 0, len(nums) -1

        #index < right is not correct 
        while index <= right:

            if nums[index] == 0 :
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                 

            if nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
                continue
                 

            index += 1

        return nums

    


"""
review session:

[x,x,x,x,x,x,x,x,x]
 L               R 
 i

 because the existence of i, L could only stops at 1;
 however, R could stops at 0, 1, 2 so it needs rearrangement

 """

