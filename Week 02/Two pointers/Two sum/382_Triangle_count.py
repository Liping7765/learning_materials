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
Review session:

1. learn how to loop backwards -> for i in range(big, small, -1)
2. How to based on the intended results to estimate the least time complexity

    a. a + b + c = 0 -> c is a constant once a + b is confirmed, so only n^2
    b. a + b <= c  -> even tho the a + b are confirmed, we still need to identify c, in this case, the 
        possible solution will be n^3

    c. however, if we only need to calculate the count, we might reduce it to n^2 or n^2 * logn 
        
3. please run thru the continue statement once to avoid logical errors

"""

