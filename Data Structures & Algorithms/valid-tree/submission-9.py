class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # An empty graph is a valid tree
        if not n:
            return True

        # Creates adjacency matrix for edges
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set() # Stores the nodes that were visited
        def dfs(i, prev):
            # If i in visit then a cycle exists
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]: # Performs dfs() on other neighbor nodes
                if j == prev: # Skips over the node that we just came from
                    continue
                if not dfs(j, i): # If cycle exists then return False
                    return False
            return True
        
        # dfs() detects if a cycle exists
        # n == len(visit) checks if the graph is connected
        # Both must be true for the graph to be a valid tree
        return dfs(0, -1) and n == len(visit)
