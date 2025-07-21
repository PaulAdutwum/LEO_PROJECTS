import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        # Undirected graph for general tests
        self.graph = Graph(directed=False)
        # Directed graph for one-way edge tests
        self.digraph = Graph(directed=True)

    def test_add_and_get_neighbors_undirected(self):
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C", weight=5)
        nbrs = self.graph.get_neighbors("A")
        self.assertIn(("B", None), nbrs)
        self.assertIn(("C", 5), nbrs)
        # Reverse edges in undirected graph
        self.assertIn(("A", None), self.graph.get_neighbors("B"))
        self.assertIn(("A", 5), self.graph.get_neighbors("C"))

    def test_add_and_get_neighbors_directed(self):
        self.digraph.add_edge("X", "Y", weight=2)
        self.assertIn(("Y", 2), self.digraph.get_neighbors("X"))
        self.assertNotIn(("X", 2), self.digraph.get_neighbors("Y"))

    def test_remove_edge_undirected(self):
        self.graph.add_edge(1, 2)
        self.graph.remove_edge(1, 2)
        self.assertNotIn((2, None), self.graph.get_neighbors(1))
        self.assertNotIn((1, None), self.graph.get_neighbors(2))

    def test_remove_edge_directed(self):
        self.digraph.add_edge("P", "Q")
        self.digraph.remove_edge("P", "Q")
        self.assertNotIn(("Q", None), self.digraph.get_neighbors("P"))

    def test_dfs_traversal(self):
        # Build A - B - C chain
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        order = self.graph.dfs("A")
        self.assertEqual(order, ["A", "B", "C"])

    def test_bfs_traversal(self):
        # Build A connected to B and C
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        order = self.graph.bfs("A")
        self.assertEqual(order[0], "A")
        self.assertCountEqual(order[1:], ["B", "C"])

    def test_traversal_nonexistent(self):
        # DFS from missing node → []
        self.assertEqual(self.graph.dfs("Z"), [])
        # BFS from missing node → ["Z"]
        self.assertEqual(self.graph.bfs("Z"), ["Z"])

    def test_weighted_edges(self):
        self.graph.add_edge("U", "V", weight=10)
        self.graph.add_edge("V", "W", weight=20)
        self.assertEqual(self.graph.get_neighbors("U"), [("V", 10)])
        self.assertEqual(
            sorted(self.graph.get_neighbors("V")),
            sorted([("U", 10), ("W", 20)])
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)