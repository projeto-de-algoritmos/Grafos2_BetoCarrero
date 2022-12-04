from typing import List, Dict
import pandas as pd

class FileController:
    def __init__(self, name: str) -> None:
        self.path = 'static/db/' + name
        self.df = pd.read_csv(self.path)

    def extract_nodes(self) -> List[str]:
        nodes = self.df['Local'].tolist()
        return nodes

    def extract_init_graph(self) -> List[Dict[str, Dict[str, int]]]:
        init_graph = self.df.set_index('Destino').groupby('Origem').apply(lambda x: x.Peso.to_dict()).to_dict()
        return init_graph