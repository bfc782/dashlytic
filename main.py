from dash import Dash

from app.callbacks import get_callbacks
from app.components import Components
from app.data import df_fake_data as data
from app.layout import get_layout


app = Dash()

def serve_layout():
    layout = get_layout(data)
    return layout

components = Components(data)
app.layout = serve_layout

_ = get_callbacks(components)

if __name__ == '__main__':
    app.run(debug=True)
