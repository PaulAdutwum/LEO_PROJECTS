from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        """
        Initialize an empty Graph.
    
        """
        self.adj = defaultdict(list) 
        self.directed = directed

    def add_edge(self, source, destination, weight=None):
        """
        Add an edge from source to destination with optional weight.
        If the graph is undirected, also adds the reverse edge.
        """
        self.adj[source].append((destination, weight))
        if not self.directed:
            self.adj[destination].append((source, weight))

    def remove_edge(self, source, destination):
        """
        Remove the edge from source to destination.
        If undirected, also removes the reverse edge.
        """
        self.adj[source] = [(nbr, w) for nbr, w in self.adj[source] if nbr != destination]
        if not self.directed:
            self.adj[destination] = [(nbr, w) for nbr, w in self.adj[destination] if nbr != source]

    def get_neighbors(self, vertex):
        """
        Return a list of (neighbor, weight) pairs for the given vertex.
        """
        return list(self.adj.get(vertex, []))

    def dfs(self, start_vertex):
        """
        Perform Depth-First Search (DFS) from start_vertex.
        Returns the list of visited vertices in DFS order.
        """
        visited = set()
        order = []

        def _dfs(v):
            visited.add(v)
            order.append(v)
            for nbr, _ in self.adj.get(v, []):
                if nbr not in visited:
                    _dfs(nbr)

        if start_vertex in self.adj:
            _dfs(start_vertex)
        return order

    def bfs(self, start_vertex):
        """
        Perform Breadth-First Search (BFS) from start_vertex.
        Returns the list of visited vertices in BFS order.
        """
        visited = set([start_vertex])
        order = []
        queue = deque([start_vertex])

        while queue:
            v = queue.popleft()
            order.append(v)
            for nbr, _ in self.adj.get(v, []):
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        return order
