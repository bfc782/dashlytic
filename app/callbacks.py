from dash import callback, Output, Input


# fmt: off
def get_callbacks(components):
    @callback(
        Output("graph-content", "figure"),
        Input("dropdown-selection", "value")
    )
# fmt: on
    def update_graph(value):
        fig = components.filter_data(value)
        return fig
