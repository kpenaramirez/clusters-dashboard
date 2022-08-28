import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.PROPMOTION_GRAPH, "children"),
        Input(ids.CLUSTER_SELECTION_DROPDOWN, "value"),
    )
    def update_propmotion_graph(cluster_name: str) -> html.Div:
        data = source.get_data(cluster_name)
        fig = px.scatter(
            data,
            x=DataSchema.PMRA,
            y=DataSchema.PMDEC,
            error_x=DataSchema.EPMRA,
            error_y=DataSchema.EPMDEC,
            color=DataSchema.PLX,
            color_continuous_scale=px.colors.sequential.Viridis,
            hover_data=[
                DataSchema.PMRA,
                DataSchema.PMDEC,
            ],
        )
        # fig["layout"]["yaxis"]["scaleanchor"] = "x"
        fig.update_traces(error_x=dict(color="gray", width=0, thickness=1))
        fig.update_traces(error_y=dict(color="gray", width=0, thickness=1))
        return html.Div(dcc.Graph(figure=fig), id=ids.PROPMOTION_GRAPH)

    return html.Div(id=ids.PROPMOTION_GRAPH)