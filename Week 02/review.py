
"""

Part 1 : Two Pointers 

1. 同向双指针

2. 相向双指针 
    a. Reverse
    b. Two sum  -> see part two 
    c. Partition -> see part three

3. 背向双指针


Part 2: Two sum 

    1. two pointers + sorted array 
        - alternatives could be threesum, or four. overall, just additional loops with two sum solution.
        - sometimes the goal is to reduce the O(n^3) to O(n^2) or O(n^2logn) eg.count of triangles
        
    2. hashmap 

    a. Within a sorted array, how do you skip the identical pairs when finding two sum?
    b. How do you find out divide and conquer when given time complexity estimate? 
    c. can you perform time complexity and space complexity analysis between method 1 and 2?
    d. why we need O(n^3) when finding combos of a + b <= c?
    e. why we need O(n^2) when finding combos of a + b + c = 0?

Part 3: Partition

    a. how to iterate a for loop backward ?
    b. why left <= right ?
    c. how can we leaping [AAAABBB] to [ABABABA]? What about [AAAABBBB]?
    d. what are the features of partition comparing mergesort? 



Part 4 Binary Search 四重境界

    a. binary search（无死循环）

    b. binary search on sorted array 
    
    eg. [oooooOXxxxx]

        [1,2,3,4,5,5,5,6,7]  k = 5

        4 -> the greatest number that is less than k
        the leftmost 5  -> the smallest number that is ">= k"
        the rightmost 5  -> the greatest number that is "<= k"
        6 -> the smallest number that is greater than k
        index of rightmost 5 - leftmost 5 -> the number of occurrence of k 
        
    c. binary search on unsorted array 

    d. binary search on answer set 
        eg. 
        1. sometimes the input array is only there for you to find possible answer range.
        2. and the answer range is the sorted array that you want to binary search with.
        3. in order to be comparison to narrow down the range, the answer range needs to have a positive/negative
        correlation to the value that needs to be compared.
        
"""
        

