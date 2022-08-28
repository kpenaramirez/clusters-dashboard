from dash import Dash, dcc, html

from src.components.dropdown_helper import to_dropdown_options
from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        children=[
            html.H6("Cluster Selection"),
            dcc.Dropdown(
                id=ids.CLUSTER_SELECTION_DROPDOWN,
                options=to_dropdown_options(source.all_clusters),
                value=source.unique_clusters,
                multi=False,
            ),
        ]
    )
