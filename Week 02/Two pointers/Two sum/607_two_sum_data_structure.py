#Hash Table 

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.data = {}

    def add(self, number):
        # write your code here
        self.data[number] = self.data.get(number, 0) + 1


    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for key in self.data:
            if key == value - key and self.data[key] == 1:
                continue 

            if value - key in self.data:
                return True 

        return False
                
            
             
"""
Error: 
1. line 23 - 25: didn't think in a logical way to set up the conditions properly.

class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}
        
    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)


Comments:

排序数组+双指针的算法会超时，但是大家可以看看是怎么写的
add  O(n) 
-> X binary search + insert  
-> X linked-list + binary search 
-> X Heap 
-> X TreeMap  

find O(n)

hashmap -> add O(1), find O(n)

        
"""
    


