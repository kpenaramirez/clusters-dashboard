import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.CMD_GRAPH, "children"),
        Input(ids.CLUSTER_SELECTION_DROPDOWN, "value"),
    )
    def update_propmotion_graph(cluster_name: str) -> html.Div:
        data = source.get_data(cluster_name)
        fig = px.scatter(
            data,
            x=DataSchema.J_K,
            y=DataSchema.MK,
            color=DataSchema.PROBABILITY,
            color_continuous_scale=px.colors.sequential.Sunsetdark,
            hover_data=[
                DataSchema.J_K,
                DataSchema.MK,
            ],
        )
        fig["layout"]["yaxis"]["autorange"] = "reversed"
        # fig["layout"]["yaxis"]["scaleanchor"] = "x"
        return html.Div(dcc.Graph(figure=fig), id=ids.CMD_GRAPH)

    return html.Div(id=ids.CMD_GRAPH)