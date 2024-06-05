from dash import callback, Output, Input


# fmt: off
def get_callbacks(components):
    @callback(
        Output("dropdown-selection", "options"),
        Output("dropdown-selection", "value"),
        Output("graph-content", "figure"),   
        Output("table-content", "columns"), 
        Output("table-content", "data"),
        Input("dropdown-selection", "value")
    )
# fmt: on
    def update_graph(value):
        components.filter_data(value)
        dropdown_options = components.get_dropdown_options()
        fig = components.get_line_plot()
        table = components.get_dash_table()
        return dropdown_options, value, fig, table.columns, table.data
