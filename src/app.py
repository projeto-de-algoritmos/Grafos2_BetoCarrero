from flask import Flask, render_template, request
from controller.file import FileController
from controller.graph import GraphController

nodes_file = FileController('posicao.csv')
nodes = nodes_file.extract_nodes()

graph_file = FileController('NodesBeto.csv')
init_graph = graph_file.extract_init_graph()

controller = GraphController(nodes, init_graph)

app = Flask(__name__)

@app.route('/caminho', methods=["POST"])
def caminho():
    start_node = str(request.form.get('start'))
    target_node = str(request.form.get('target'))

    previous_nodes, _ = controller.graph.dijkstra_algorithm(start_node=start_node) 
    path = controller.get_path(previous_nodes, start_node=start_node, target_node=target_node)

    return render_template('caminho.html',path=path)

@app.route('/', methods=["GET"])
def index():
    return render_template('base.html',nodes=nodes)
        
