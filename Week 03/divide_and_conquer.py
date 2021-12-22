#divide and conquer 

def divideConquer(root):

    if not root:
        return None

    """
    if not root.left and root.right :
        处理叶子应该返回的结果
        如果叶子的返回结果可以通过两个空节点返回得到，
        就可以省略这一段代码
    """ 
    
    left = divideConquer(root.left)
    right = divideConquer(root.right)

    whole = left + right (could be any way of combination or comparison)

    return whole 


"""
note: when there is simple return value, this method could be effective


difference between traversal and divide&conquer is below,
    a. traversal uses global variables or shared arguments 
    b. divide&conquer uses return value as the result
    c. divide&conquer is post-order dfs 

"""

