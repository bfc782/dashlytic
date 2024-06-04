from dash import Dash, callback, Output, Input
import plotly.express as px

from app.data import df_fake_data as data
from app.layout import get_layout


app = Dash()

def serve_layout():
    layout = get_layout(data)
    return layout

app.layout = serve_layout

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):

    dff = data[data.customer==value]
    fig = px.line(dff, x='transaction_date', y='amount')
    fig.update_xaxes(type='date', tickformat='%Y-%m-%d', tickvals=dff['transaction_date'])
    fig.update_yaxes(range=[0, 200])
    return fig

if __name__ == '__main__':
    app.run(debug=True)