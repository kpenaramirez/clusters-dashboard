from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_cluster_data
from src.data.source import DataSource

DATA_PATH = "./data/starclusters.csv"

def main() -> None:

    data = load_cluster_data(DATA_PATH)
    data = DataSource(data)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = r"Clusters from Peña Ramírez et al. 2020 and 2021"
    app.layout = create_layout(app, data)
    
    return app


app = main()
server = app.server

if __name__ == "__main__":
     app.run_server(host="0.0.0.0", port=8050, debug=False)
