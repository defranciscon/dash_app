from dash import dash_table
from webapp.pages.data.models import dff, display_columns

data_table = dash_table.DataTable(
            id='datatable',
            columns=display_columns,
            data=dff.to_dict('records'),
            filter_action="native",
            editable=False,
            sort_action="native",
            sort_mode="multi",
            selected_rows=[],
            selected_columns=[],
            column_selectable="single",
            row_selectable="single",
            page_action="native",
            page_current=0,
            page_size=20,
            style_table={'overflowX':'auto'},
            fixed_rows={'headers': True},
            style_cell={
                'textAlign': 'left',
                'font-size': 18,
                'width': '{}%'.format(len(dff.columns)),
                'textOverflow': 'ellipsis',
                'overflow': 'hidden'
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'white',
                'whiteSpace': 'normal',
                'height': 'auto'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(220, 220, 220)',
                }
            ],
            style_header={
                'backgroundColor': 'rgb(210, 210, 210)',
                'color': 'black',
                'fontWeight': 'bold'
                },
            )