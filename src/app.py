from flask import Flask, render_template
from controller.file import FileController

nodes_file = FileController('posicao.csv')
nodes = nodes_file.extract_nodes()

graph_file = FileController('NodesBeto.csv')
init_graph = graph_file.extract_init_graph()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')
