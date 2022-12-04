from flask import Flask, render_template, request
from controller.file import FileController
from controller.graph import GraphController

import os
import cv2

nodes_file = FileController('posicao.csv')
nodes = nodes_file.extract_nodes()
positions = nodes_file.extract_positions()

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

    for filename in os.listdir('./static/images/'):
        if filename.startswith('path_'):  
            os.remove('./static/images/' + filename)

    position = []
    for local in path:
        position.append(positions[local])

    image = cv2.imread('./static/images/mapa-beto-carrero-world.png')

    for i in position:
        cv2.line(image, i[0], i[1], (0,0,255), 2)

    new_image_name = "path_" + start_node + '_' +  target_node + ".png"
    cv2.imwrite("./static/images/" + new_image_name, image)

    return render_template('base.html',nodes=nodes, path=path, image= "images/" + new_image_name)

@app.route('/', methods=["GET"])
def index():
    return render_template('base.html',nodes=nodes)
        
