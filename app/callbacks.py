from dash import callback, Output, Input


# fmt: off
def get_callbacks(components):
    @callback(
        Output("graph-content", "figure"),
        Input("dropdown-selection", "value")
    )
# fmt: on
    def update_graph(value):
        components.filter_data(value)
        fig = components.get_line_plot()
        return fig
