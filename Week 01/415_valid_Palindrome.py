#双指针

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here

        #validate the input 
        if not s:
            return True 

        #initiate two pointer as i and j 
        i, j = 0, len(s) - 1

        #go through the string until i and j pass each other 

        while(i <= j):

            #skip the invalid char
            if not self.is_valid(s[i]):
                i += 1
                continue 
            if not self.is_valid(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower() :
                return False 

            #if two pointers are the same, we move closer one step 
            i += 1
            j -= 1

        return True 



    #write a subfunction to varify if the char is valid

    def is_valid(self, letter):
        return letter.isalpha() or letter.isdigit()


"""
errors:
1. j -= 1 was written mistakenly as j += 1
2. should think of sub function to reduce repeated codes 

Comments:
1. string.isdigit()
2. string.isalpha()
3. string.upper() 
4. string.lower()
5. should think of sub function to reduce repeated codes 

"""



