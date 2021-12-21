"""
1. How to loop backwards?

my_list = [1, 2, 3]
my_list.reverse()           # my_list is modified
print(my_list)              # '[3, 2, 1]'
my_revert = my_list[::-1]   # my_list stays [3, 2, 1]
print(my_revert)            # '[1, 2, 3]'



# Item by item reverse with range(<start>, <end>, <step>)
for i in range(len(my_list), 0, -1):		# my_list is [3, 2, 1]
    print(my_list[i-1])		# '1' '2' '3'


    
for i in reversed(range(len(my_list))):
    print(my_list[i])       # '1' '2' '3'



2. peak value summary 


3. Breath First Search 
- 分层遍历 （最短路径）
- 从一点分散找到所有连接块 （isolated island） 
- 拓扑排序

实现方法
-单队列
-双队列
-dummy node

4. binary search tree 

Smallest node : leftmost of the tree 

next node in order or smallest node that is greater than one node : 
1.the leftmost node of the right sub tree 
2. the first parent node whose node.left contains the starting node 

阅读全文并背诵 13. BST iterator


5. sum(wood // k for wood in L)

"""