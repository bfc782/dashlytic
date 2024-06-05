import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table


def get_layout():
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
                            dcc.Dropdown(id="dropdown-selection", multi=True),
                            dcc.Graph(id="graph-content"),
                            dash_table.DataTable(id="table-content"),
                        ]
                    ),
                ]
            ),
        ]
    )
