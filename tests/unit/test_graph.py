import sys 
sys.path.append("src/") 

from controller.file import FileController
from controller.graph import GraphController
import unittest

class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:
        nodes_file = FileController('posicao.csv', 'src/static/db/')
        nodes = nodes_file.extract_nodes()

        graph_file = FileController('NodesBeto.csv', 'src/static/db/')
        init_graph = graph_file.extract_init_graph()

        self.controller = GraphController(nodes, init_graph)

    def test_previvous_nodes(self):
        expected_previous_nodes = {
            'Mascotes': 'Entrada', 
            'Lilica e tigor': 'Mascotes', 
            'Alimentacao': 'Mascotes', 
            'Aldeia': 'Mascotes', 
            'Raskapuska': 'Alimentacao', 
            'Chapeu': 'Aldeia', 
            'Hipica': 'Aldeia', 
            'Vila germanica': 'Lilica e tigor', 
            'Sonho do cowboy': 'Chapeu', 
            'Mundo animal': 'Chapeu', 
            'Casa mal assombrada': 'Hipica', 
            'Ilha dos piratas': 'Vila germanica', 
            'Zoologico': 'Mundo animal', 
            'Mundo da fantasia': 'Mundo animal', 
            'Firewhip': 'Mundo animal', 
            'Barco pirata': 'Ilha dos piratas', 
            'Hot wheels': 'Mundo da fantasia', 
            'Tchibum': 'Firewhip'}
        previous_nodes, _ = self.controller.graph.dijkstra_algorithm(start_node="Entrada") 
        self.assertEqual(expected_previous_nodes, previous_nodes)

    def test_shortest_path(self):
        expected_shortest_path = {
            'Entrada': 0, 
            'Mascotes': 12, 
            'Lilica e tigor': 34, 
            'Alimentacao': 21, 
            'Aldeia': 22, 
            'Vila germanica': 42, 
            'Ilha dos piratas': 63, 
            'Raskapuska': 30, 
            'Barco pirata': 75, 
            'Chapeu': 32, 
            'Sonho do cowboy': 45, 
            'Mundo animal': 59, 
            'Hipica': 34, 
            'Casa mal assombrada': 49, 
            'Zoologico': 73, 
            'Mundo da fantasia': 91, 
            'Firewhip': 113, 
            'Hot wheels': 108, 
            'Tchibum': 126}
        _, shortest_path = self.controller.graph.dijkstra_algorithm(start_node="Entrada") 
        self.assertEqual(expected_shortest_path, shortest_path)

    def test_get_path(self):
        expected = ['Entrada', 'Mascotes', 'Aldeia', 'Chapeu']
        previous_nodes, _ = self.controller.graph.dijkstra_algorithm(start_node="Entrada") 
        path = self.controller.get_path(previous_nodes, start_node="Entrada", target_node="Chapeu")
        self.assertEqual(expected, path)

    def test_get_path(self):
        expected = ['Aldeia', 'Chapeu', 'Sonho do cowboy']
        previous_nodes, _ = self.controller.graph.dijkstra_algorithm(start_node="Aldeia") 
        path = self.controller.get_path(previous_nodes, start_node="Aldeia", target_node="Sonho do cowboy")
        self.assertEqual(expected, path)
    