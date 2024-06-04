from dash import Dash

from app.callbacks import get_callbacks
from app.components import Components
from app.data import df_fake_data as data
from app.layout import get_layout


app = Dash()

components = Components(data)

def serve_layout():
    layout = get_layout(components)
    return layout

app.layout = serve_layout

_ = get_callbacks(components)

if __name__ == '__main__':
    app.run(debug=True)
