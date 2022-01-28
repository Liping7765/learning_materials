import heapq

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        gragh = self.create_graph(words)

        return self.topo_sort(graph)

    
    def create_graph(self, words):
        
        graph = {}
        #create a graph for each letter in words
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = set()

        for i in range(len(words)-1):

            word_length = min(len(words[i]), len(words[i + 1]))
            for j in range(word_length):
                #add the first different letter to the graph 
                if words[i][j] != words[i + 1][j]:

                    graph[word[i][j]].add(words[i + 1][j])
                    break 

                #edge case: "abc" in front of "ab", the ranking should be invalid 
                if j == word_length - 1 and len(words[i]) < len(words[i + 1]):
                    return None 

        
        return graph 
        
            

    def in_degree(self, graph):
        
        degree = {}

        for key in graph.keys():
            degree[key] = 0

        #calculate the degree for each letter 
        for each in graph.values():
            for letter in each:
                degree[letter] += 1

        return degree
       

    def topo_sort(self, graph):

        if graph == None:
            return ""
        
        in_degree = self.in_degree(graph)

        #find the ones with zero in-degree
        queue = []
        heapq.heapify(queue)

        for key, value in in_degree.items():
            if value == 0:
                queue.heappush(key)

        result = ""
        while queue:

            temp = queue.heappop()
            result += temp 

            for letter in graph[temp]:
                in_degree[letter] -= 1
                if in_degree[letter] == 0:
                    queue.heappush(letter)


        return result if len(result) == len(graph) else ""