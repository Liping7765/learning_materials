
# distance 有两个作用，一是查重，二是记录节点到root的距离
queue = collections.deque([node])
distance = {node : 0}


while queue:

    node = queue.popleft()

    for neighbor in node.get_neighbors():

        if neighbor in distance:
            continue 

        #比原来的node多一层，估加一
        distance[neighbor] = distance[node] + 1
        queue.append(neighbor)


#时间复杂度为 O(M + N), M为边，N为点

