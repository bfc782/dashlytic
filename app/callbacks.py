from dash import callback, Output, Input, State


# fmt: off
def get_callbacks(components):
    @callback(
        Output("dropdown-filter-selection", "options"),
        Input("dropdown-dim-selection", "value"),
    )
    def update_dim(dim_selected):
        dropdown_options = components.get_dropdown_options(dim_selected)
        return dropdown_options

    @callback(
        Output("graph-content", "figure"),   
        Output("table-content", "columns"), 
        Output("table-content", "data"),
        State("dropdown-dim-selection", "value"),
        Input("dropdown-filter-selection", "value"),
    )
# fmt: on
    def update_graph(col, value):
        dim_options = components.data_dims
        components.filter_data(col, value)
        dropdown_options = components.get_dropdown_options(col)
        fig = components.update_graph(col)
        table = components.update_table()
        return dim_options, dropdown_options, value, fig, table.columns, table.data
