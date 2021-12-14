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


"""