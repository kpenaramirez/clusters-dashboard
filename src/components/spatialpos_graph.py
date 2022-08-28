import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.SPATIALPOS_GRAPH, "children"),
        Input(ids.CLUSTER_SELECTION_DROPDOWN, "value"),
    )
    def update_spatialpos_graph(cluster_name: str) -> html.Div:
        data = source.get_data(cluster_name)
        fig = px.scatter(
            data,
            x=DataSchema.RA,
            y=DataSchema.DEC,
            color=DataSchema.PROBABILITY,
            color_continuous_scale=px.colors.sequential.Sunsetdark,
            hover_data=[
                DataSchema.RA,
                DataSchema.DEC,
            ],
        )
        # fig["layout"]["yaxis"]["scaleanchor"] = "x"
        return html.Div(dcc.Graph(figure=fig), id=ids.SPATIALPOS_GRAPH)

    return html.Div(id=ids.SPATIALPOS_GRAPH)