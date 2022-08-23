import pandas as pd
from dash import Dash, html
from src.components import (
    cluster_selection_dropdown
)


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-cointainer",
                children=[
                    cluster_selection_dropdown.render(app, data)
                ],
            ),
        ],
    )