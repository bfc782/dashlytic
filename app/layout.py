import dash_bootstrap_components as dbc
from dash import html


def get_layout(components):
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
                            components.dropdown,
                            components.graph,
                            components.table,
                        ]
                    ),
                ]
            ),
        ]
    )
