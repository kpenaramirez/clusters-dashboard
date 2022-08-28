import pandas as pd
from dash import Dash, html
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
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-cointainer",
                children=[
                    cluster_selection_dropdown.render(app, source),
                    probability_rangeselector.render(app),
                ],
            ),
            html.Pre(id="test_output_pre"),  # TODO: Remove
            spatialpos_graph.render(app, source),
            propmotion_graph.render(app, source),
            cmd_graph.render(app, source),
        ],
    )
