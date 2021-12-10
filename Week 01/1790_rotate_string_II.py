class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here

        if not str:
            return str

        final = (left - right) % len(str)

        return str[final:] + str[:final]



"""
review session
1.Python can have negative index.
"""

