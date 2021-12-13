# Binary search 
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here

        return self.binary_search(nums, 0, len(nums)-1, target)


    
    def binary_search(self, nums, start, end, target):

        #base case 
        if start > end:
            return -1
    
        middle = (start + end) // 2

        if nums[middle] == target:
            return middle 


        if nums[middle] > target:

            return self.binary_search(nums, start, middle - 1, target)

        return self.binary_search(nums, middle + 1, end, target)


#template 
# while left + 1 < right

# it will just result an array with length of two, we can identify the numbers based on our requirements from there. 

