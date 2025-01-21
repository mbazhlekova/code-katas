import collections

class Solution:
    # Create an adjacency list for each node - basically what nodes it connects to
    def adjacencyList(self, edges):
        adjList = {}

        for src, dst in edges:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)

        return adjList
    
    # Count paths - backtracking, depth-first search
    # Not very efficient due to size of graph growing
    def dfs(self, node, target, adjList, visit):
        # If node has already been visited, there are 0 paths from node to result?
        # Still unclear on this part
        if node in visit:
            return 0
        # If this is the target, means we have found a path and can return 1
        # because we are just getting a count of the number of paths
        if node == target:
            return 1
        
        # Declare a variable to keep count of how many paths from start node to target
        count = 0
        # Add node to hash set 
        visit.add(node)
        # Go through its list of neighbors
        for neighbor in adjList[node]:
            count += self.dfs(neighbor, target, adjList, visit)
        visit.remove(node)

        return count
    
    # Find the shortest path from node to target 🤦🏻‍♀️
    def bfs(node, target, adjList):
        length = 0
        visit = set()
        visit.add(node)
        queue = collections.deque()
        queue.append(node)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return length
            
                for neighbor in adjList[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)
            length += 1
        
        return length

    
tmp = Solution
print(tmp.adjacencyList(tmp, [["A", "B"], ["B", "C"], ["B", "E"], ["C","E"], ["E", "D"]]))
