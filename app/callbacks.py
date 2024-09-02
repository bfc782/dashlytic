from dash import callback, Output, Input, State


# fmt: off
def get_callbacks(components: object):
    @callback(
        Output("dropdown-dim-selection", "options"),
        Output("dropdown-dim-selection", "value"),
        Input("dropdown-dim-selection", "value"),
    )
    def update_dim(dim_selected: str) -> list:
        dropdown_options = components.data_dim_options
        dropdown_value = components.dropdown_dim.value
        return dropdown_options, dropdown_value

    @callback(
        Output("graph-content", "figure"), 
        Output("dropdown-filter-selection", "options"),  
        Output("table-content", "columns"), 
        Output("table-content", "data"),
        Input("dropdown-dim-selection", "value"),
        Input("dropdown-filter-selection", "value"),
    )
# fmt: on
    def update_graph(col: str, value: str) -> list:
        # dim_options = components.data_dim_options
        components.get_data_dim(col)
        dropdown_options = components.get_dropdown_options(col)
        fig = components.update_graph()
        table = components.update_table()
        return fig, dropdown_options, table.columns, table.data


'''

import inspect
import your_module

classes = [member for member in dir(your_module) if inspect.isclass(getattr(your_module, member))]
print(classes)


defined_classes = [
    member for member in dir(your_module) 
    if inspect.isclass(getattr(your_module, member)) and getattr(your_module, member).__module__ == your_module.__name__
]

print(defined_classes)

'''