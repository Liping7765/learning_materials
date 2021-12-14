class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here

        nums = sorted(S)
        result = 0

        for i in range(len(nums) - 1, 0, -1) : 

            result += self.count_twosum(nums, 0, i - 1, nums[i])

        return result 


    def count_twosum(self, nums, start, end, target):

        left, right = start, end 
        count = 0

        while left < right :
            
            if nums[left] + nums[right] > target:
                count += right - left 
                right -= 1
                continue 

            left += 1

        return count 


"""

1. remember to check the continue 

2. learn how to loop backwards 

"""

