from dash import dash_table, dcc
import plotly.express as px
from typing import Optional

class Components:
    def __init__(self, data, time_ix: str = "transaction_date", measure: str = "amount"):
        self.data = data
        self.time_ix = time_ix
        self.measure = measure
        # self.time_measure = [time_ix, measure]
        self.data_dim_options = self.data.columns.unique().to_list()
        self.dropdown_dim = dcc.Dropdown(
            id="dropdown-dim-selection", value=self.data_dim_options[1], multi=False  # false for now
        )
        self.dropdown_filter = dcc.Dropdown(id="dropdown-filter-selection", multi=True)
        self.graph = dcc.Graph(id="graph-content")
        self.table = dash_table.DataTable(id="table-content")

    def get_dropdown_options(self, col):
        self.dropdown_options = self.data[col].unique()
        return self.dropdown_options

    def get_data_dim(self, col: str):
        self.data_dim = self.data[[self.time_ix, col, self.measure]]
        return self.data_dim

    def update_graph(self):
        [col] = [i for i in self.data_dim.columns.tolist() if i not in [self.time_ix, self.measure]]
        self.fig = px.line(self.data_dim, x=self.time_ix, y=self.measure, color=col)
        self.fig.update_xaxes(
            type="date", tickformat="%Y-%m-%d", tickvals=self.data[self.time_ix]
        )
        self.fig.update_yaxes(range=[0, 200])
        return self.fig

    def update_table(self):
        self.table = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in self.data.columns],
            data=self.data.to_dict("records"),
        )
        return self.table
