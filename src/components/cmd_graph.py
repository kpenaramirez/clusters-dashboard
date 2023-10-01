from typing import List
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
        Input(ids.PROBABILITY_RANGE_SELECTOR, "value"),
    )
    def update_propmotion_graph(
        cluster_name: str, probrange: tuple[float, float]
    ) -> html.Div:
        data = source.filter_data(cluster_name, probrange)

        fig = px.scatter(
            data.get_data,
            x=DataSchema.J_K,
            y=DataSchema.MK,
            color=DataSchema.PROBABILITY,
            color_continuous_scale=px.colors.sequential.Sunsetdark,
            range_color=(0.0, 1.0),
            hover_data=(
                DataSchema.STARID,
                DataSchema.J_K,
                DataSchema.MK,
            ),
            title="Color-magnitude diagram",
        )
        fig.update_layout(
            xaxis_title=r'$ J - K_S \, \text{(mag)}$',
            yaxis_title=r'$K_S \, \text{(mag)}$',
            coloraxis_colorbar_title="Probability",
            coloraxis_colorbar_title_side="top",
        )


        fig["layout"]["yaxis"]["autorange"] = "reversed"
        # fig["layout"]["yaxis"]["scaleanchor"] = "x"


        return html.Div(dcc.Graph(mathjax=True, figure=fig), id=ids.CMD_GRAPH)

    return html.Div(id=ids.CMD_GRAPH)
