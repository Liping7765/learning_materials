

#first thought is to go through the string and then compare if that matches target 
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here

        if not target:
            return 0

        if not source:
            return -1

        for index in range(len(source)-len(target)+1) :
            if source[index] != target[0]:
                continue 

            if source[index:index+len(target)]==target:
                return index 
            
        return -1

"""
    comments: python comparing the substrings letter by letter, which cause the runtime to be O(nm) where n < m 
"""

#utilized hash function to compare two strings 
#Robin Karp 
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here

        if not target:
            return 0

        if not source:
            return -1

        BASE = 1000000
        m = len(target)
        power = 31 ** m % BASE

        #find out hashed_target
        hashed_target = 0
        for letter in target:
            hashed_target = (hashed_target * 31 + ord(letter)) % BASE

        
        hashcode = 0
        for index, letter in enumerate(source):

            hashcode = (hashcode * 31 + ord(letter)) % BASE

            if index < m-1:
                continue

            if index >= m :
                hashcode = hashcode - (power * ord(source[index-m])) % BASE

            # hashcode could be negative due to substraction 
            # but we can still keep the number positive by adding one BASE
            if hashcode < 0 :
                hashcode += BASE

            """
                notes: errors occured at this last section due to unclear indexing 
                the index is representing the last letter of the string
            """
            if hashcode == hashed_target and source[index-m+1:index+1] == target:
                return index - m + 1

        return -1


"""
(A * B) mod C = (A mod C * B mod C) mod C

(A - B) mod C = (A mod C - B mod C) mod C

(A + B) mod C = (A mod C + B mod C) mod C

"""

                
"""
------------review section-------------
1.hash function 
2.modular oprations 

"""