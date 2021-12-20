class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here

        self.sort(colors, 0, len(colors) - 1, 0, k)

    
    def sort(self, colors, start, end, color_from, color_to):

        if color_from == color_to or start == end:
            return 

        # divide two sides 
        pivot_color = (color_from + color_to) // 2

        left, right = start, end 
        
        while left <= right:

            while left <= right and colors[left] <= pivot_color:
                left += 1

            while left <= right and colors[right] > pivot_color:
                right -= 1     

            
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        
        self.sort(colors, start, right, color_from, pivot_color)
        self.sort(colors, left, end, pivot_color + 1, color_to)

"""
review session: 

O(nlogk) 
-> backtrack the idea of the algorithm 
-> divide and conquer (mergesort) or -> binary sear

"""

