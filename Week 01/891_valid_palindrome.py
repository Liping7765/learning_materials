#双指针
class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        if not s or len(s) == 1:
            return True 

        left, right = self.find_differences(s, 0, len(s) - 1)

        if left >= right:
            return True 
        
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)


    def find_differences(self, s, start, end):

        while(start < end):

            if s[start] == s[end]:
                start += 1
                end -= 1
                continue 

            break

        return start, end 

    
    def is_palindrome(self, s, start, end):

        left, right = self.find_differences(s, start, end)

        return left >= right 


"""
---------review session--------

1. Use function find_differences to reduce repeated codes(two pointers to loop till the different charactors)
2. The reason we don't use recurive function is condition "at most 1 letter removed".
We only need to identify if the substring is palindrome when we encounter different chars for the first time
3. When even number, the left and right pointer will end up crossing over each other.
When odd number, loop stops at left equals to right.

"""
