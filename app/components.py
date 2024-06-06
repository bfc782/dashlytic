from dash import dash_table, dcc
import plotly.express as px


class Components:
    def __init__(self, data):
        self.data = data
        self.data_dims = self.data.columns.unique().to_list()
        self.dropdown_dim = dcc.Dropdown(
            id="dropdown-dim-selection", value=self.data_dims[1], multi=True
        )
        self.dropdown_filter = dcc.Dropdown(id="dropdown-filter-selection", multi=True)
        self.graph = dcc.Graph(id="graph-content")
        self.table = dash_table.DataTable(id="table-content")

    def get_dropdown_options(self, col):
        self.dropdown_options = self.data[col].unique()
        return self.dropdown_options

    def filter_data(self, col, value):
        if value:
            self.dff = self.data[self.data[col].isin(value)]
        else:
            self.dff = self.data

    def update_graph(self, col):
        self.fig = px.line(self.dff, x="transaction_date", y="amount", color=col)
        self.fig.update_xaxes(
            type="date", tickformat="%Y-%m-%d", tickvals=self.data["transaction_date"]
        )
        self.fig.update_yaxes(range=[0, 200])
        return self.fig

    def update_table(self):
        self.table = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in self.dff.columns],
            data=self.dff.to_dict("records"),
        )
        return self.table
