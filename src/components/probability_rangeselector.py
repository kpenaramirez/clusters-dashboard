from dash import Dash, dcc, html

from . import ids


def render(app: Dash) -> html.Div:

    return html.Div(
        children=[
            html.H6("Probability Range"),
            dcc.RangeSlider(
                min=0.0,
                max=1.0,
                value=(0.0, 1.0),
                id=ids.PROBABILITY_RANGE_SELECTOR,
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ]
    )
