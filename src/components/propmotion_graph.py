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
        Input(ids.PROBABILITY_RANGE_SELECTOR, "value"),
    )
    def update_propmotion_graph(
        cluster_name: str, probrange: tuple[float, float]
    ) -> html.Div:
        data = source.filter_data(cluster_name, probrange)
        scatter_params = {}
        scatter_params = dict(
            x=DataSchema.PMRA,
            y=DataSchema.PMDEC,
            error_x=DataSchema.EPMRA,
            error_y=DataSchema.EPMDEC,
            hover_data=[
                DataSchema.STARID,
                DataSchema.PMRA,
                DataSchema.PMDEC,
            ],
        )
        # Add extra params if the data has valid parallax data
        # print(data.count_valid_rows_by_column(column_name = "plx"))
        if data.count_valid_rows_by_column(DataSchema.PLX):
            scatter_params.update(
                dict(
                    color=DataSchema.PLX,
                    color_continuous_scale=px.colors.sequential.Viridis,
                )
            )

        fig = px.scatter(data.get_data, **scatter_params)

        fig.update_traces(
            error_x=dict(color="gray", width=0, thickness=1),
            error_y=dict(color="gray", width=0, thickness=1),
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.PROPMOTION_GRAPH)

    return html.Div(id=ids.PROPMOTION_GRAPH)
