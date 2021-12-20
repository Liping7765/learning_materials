#Two pointers
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here

        if len(numbers) < 3:
            return []

        numbers = sorted(numbers)
        results = []

        for index in range(len(numbers)):
            
            if index > 0 and numbers[index] == numbers[index - 1]:
                continue 
            
            self.twosum(numbers, index + 1, len(numbers) - 1, -numbers[index], results)

        return results


    
    def twosum(self, numbers, start, end, target, results):

        last_pair = None
        left, right = start, end 

        while left < right:

            if numbers[left] + numbers[right] == target:

                if (numbers[left], numbers[right]) != last_pair:

                    
                    results.append([-target, numbers[left], numbers[right]])
                    
                last_pair = (numbers[left], numbers[right])
                left += 1
                right -= 1

            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        



"""
errors:
1. forgot to move forward when append the result to the list 
2. should use one variable to store the previous pair to avoid duplicates 
3. -target is actually the first element of the combination 
4. "if index > 0 and numbers[index] == numbers[index - 1]:" to avoid duplicates 

comments: 
for error 2 and 4 are actaully utizling the characteristic of a sorted array 
[1,1,1,2] -> [1,2]
[1,1,2,2] -> [1,1,2,2] 
 L     R        L R

重要考点应该是 “去重”
不应该依赖hashset本来去把结果去重，本身得到结果的过程会产生多次重复

Hashset itself is for find existence of elements 

"""


    

            
            

        
