import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_clusters = sorted(data[DataSchema.CLUSTER].unique().tolist())

    return html.Div(
        children=[
            html.H6("Cluster Selection"),
            dcc.Dropdown(
                id=ids.CLUSTER_SELECTION_DROPDOWN,
                options=[{"label": cluster.replace("_", " "), "value": cluster} for cluster in all_clusters],
                value=all_clusters[0],
            )
        ]
    )
        