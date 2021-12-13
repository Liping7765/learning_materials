# when using python, if the variable is not being used in the block, we use '_' to indicate that. 

for _ in range(100):
    print('just need to print this a hundred times')


#Substring    "andfslkjl" -> "and" (consecutive)
#Subsequence   "asdflsj"  -> "aj" (inconsecutive)


#时间复杂度
"""
Based on O(n), we can aim at below algorithm 
two pointers 
打擂台
stack
Queue 
"""

#双指针
相向双指针（最常用）
    1.Reverse
        -翻转字符串
        -判断回文串
    2.Two Sum
        -两数之和
        -三数之和
    3.Partition 
        -快速排序
        -颜色排序
背向双指针
同向双指针


"""
Recursion
1. 函数应该接受什么样的参数，返回什么样的值，代表什么意思
2. 递归的拆解
3. 递归的出口

"""


"""
How to create a array with a certain length in python:
nums = [0] * n  

1.The arguments, the return values, and variable "nums" itself is stored in stack space, 
however, the numbers in nums are actually stored in heap space to avoid stack overflow. 

2.Content stored in stack space will be erased after function ends, but heap space will remain.

3.尾递归可以实现O（1）的空间消耗
""""

