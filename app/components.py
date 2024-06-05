from dash import dash_table, dcc
import plotly.express as px


class Components:
    def __init__(self, data):
        self.data = data
        self.dropdown = dcc.Dropdown(id="dropdown-selection", multi=True)
        self.graph = dcc.Graph(id="graph-content")
        self.table = dash_table.DataTable(id="table-content")

    def get_dropdown_options(self):
        self.dropdown_options = self.data["customer"].unique()
        return self.dropdown_options

    def filter_data(self, value):
        if value:
            self.dff = self.data[self.data["customer"].isin(value)]
        else:
            self.dff = self.data

    def update_graph(self):
        self.fig = px.line(self.dff, x="transaction_date", y="amount", color="customer")
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
