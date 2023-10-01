import pandas as pd
from dash import Dash, html, dcc
from src.components import (
    cluster_selection_dropdown,
    spatialpos_graph,
    propmotion_graph,
    cmd_graph,
    probability_rangeselector,
)

from ..data.source import DataSource


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            dcc.Markdown(f"# {app.title}", mathjax=True),
            dcc.Markdown(f"> Open clusters studied in Peña Ramírez et al. (2021, 2022)"),
            html.Div(
                className="dropdown-cointainer",
                children=[
                    cluster_selection_dropdown.render(app, source),
                    probability_rangeselector.render(app),
                ],
            ),
            html.Div(
                className="graph-container",
                children=[
                    spatialpos_graph.render(app, source),
                    propmotion_graph.render(app, source),
                    cmd_graph.render(app, source),
                ],
            ),
        ],
    )
