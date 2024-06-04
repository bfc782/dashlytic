from dash import dash_table
import plotly.express as px


class Components:
    def __init__(self, data):
        self.data = data

    def filter_data(self, value):
        self.dff = self.data[self.data["customer"] == value]
    
    def get_line_plot(self):
        self.fig = px.line(self.dff, x="transaction_date", y="amount")
        self.fig.update_xaxes(
            type="date", tickformat="%Y-%m-%d", tickvals=self.data["transaction_date"]
        )
        self.fig.update_yaxes(range=[0, 200])
        return self.fig


