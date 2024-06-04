import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table


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
                            dcc.Dropdown(
                                components.data.customer.unique(),
                                "",
                                id="dropdown-selection",
                            ),
                            dcc.Graph(id="graph-content"),
                            dash_table.DataTable(id="table-content"),
                        ]
                    ),
                ]
            ),
        ]
    )
