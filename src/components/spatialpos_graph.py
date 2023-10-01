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
        Input(ids.PROBABILITY_RANGE_SELECTOR, "value"),
    )
    def update_spatialpos_graph(
        cluster_name: str,
        probrange: tuple[float, float],
    ) -> html.Div:
        data = source.filter_data(cluster_name, probrange)

        fig = px.scatter(
            data.get_data,
            x=DataSchema.RA,
            y=DataSchema.DEC,
            color=DataSchema.PROBABILITY,
            color_continuous_scale=px.colors.sequential.Sunsetdark,
            range_color=(0.0, 1.0),
            hover_data=(
                DataSchema.STARID,
                DataSchema.RA,
                DataSchema.DEC,
            ),
            title="Spatial position",
        )

        fig.update_layout(
            xaxis_title=r'$\alpha \, \text{(deg)}$',
            yaxis_title=r'$\delta \, \text{(deg)}$',
            coloraxis_colorbar_title=r'Probability',
            coloraxis_colorbar_title_side="top",
        )
        
        return html.Div(dcc.Graph(mathjax=True, figure=fig), id=ids.SPATIALPOS_GRAPH)


    return html.Div(id=ids.SPATIALPOS_GRAPH)
