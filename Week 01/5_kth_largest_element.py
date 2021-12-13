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


#successful attempt
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

        if start == end:
            return nums[start]

        #initialize a pivot 
        pivot = nums[(start + end) // 2]
        left, right = start, end 
        # find its right position of the array

        while(left <= right): #see below comment 1

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

        if left <= len(nums) - k:
            return self.quickselect(k, nums, left, end)

        if right >= len(nums) - k:
            return self.quickselect(k, nums, start, right)

        
        return nums[left - 1]


"""
1. Three possible results due to this condition:

scenario 1 : [right, pivot, left]
scenario 2 : [right, left/pivot]  ---coming from [left(pivot), right(smaller than pivot)] ---swap---> 
scenario 3 : [pivot/right, left]  ---coming from [left(greater than pivot), right(pivot)] ---swap---> 



2. python built-in trick : a, b = b, a

3. What would happen if we set "while left < right :" ?

scenario 1 : [right/pivot/left]
scenario 2 : [right, left/pivot]  ---coming from [left(pivot), right(smaller than pivot)] ---swap---> 
scenario 3 : [pivot/right, left]  ---coming from [left(greater than pivot), right(pivot)] ---swap---> 

scenario 1 would cause [0,1] to occur stack overflow.
    left = 0, pivot = 0, right = 1 
    -> 
    left = 0, pivot = 0, right = 0
    ->
    if we take [left, end] again, will just go back to the first step 
       

"""

