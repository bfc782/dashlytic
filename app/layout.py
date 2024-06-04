import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px


def get_layout(data):
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                children="Transaction Analysis",
                                style={"textAlign": "center"},
                            )
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                data.customer.unique(), "", id="dropdown-selection"
                            ),
                            dcc.Graph(id="graph-content"),
                        ]
                    ),
                ]
            ),
        ]
    )
