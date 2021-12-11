#quick select 
#Failed Attempt 

class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        # write your code here

        return self.quickselect(k, nums, 0, len(nums) - 1)
  
    def quickselect(self, k, nums, start, end):

        #initialize a pivot 
        pivot = nums[(start + end) // 2]
        left, right = start, end 
        # find its right position of the array

        while(left <= right):

            if nums[left] < pivot:
                left += 1
                continue 
            
            if nums[right] > pivot:
                right -= 1
                continue 

            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1 

        #if postion is smaller than K, find the right array 
        if left - 1 < len(nums) - k :

            return self.quickselect(k, nums, left, end)

        #if postion is bigger than K, find the left array 

        if right - 1 > len(nums) - k:

            return self.quickselect(k, nums, start, right)
        #if equals to k, return the value 
        return nums[left - 1]
