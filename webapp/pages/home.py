import dash 
import dash_leaflet as dl
import plotly.express as px
import pandas as pd
from dash import Input, Output, html, dcc, callback
from webapp.pages.data.models import df_filter, dff, display_columns
from webapp.pages.layouts.dashboard import DASHBOARD

dash.register_page(__name__, path='/')

# Home page layout to display the main dashboard components
layout = html.Div(
    style={'padding': '30px'},
    children=[DASHBOARD]
)

@callback(Output('datatable', 'style_data_conditional'),Input('datatable', 'selected_columns'))
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]
    
@callback([Output('datatable', 'data', allow_duplicate=True),
          Output('datatable', 'columns', allow_duplicate=True)],
          Input('reset-rescue-button', 'n_clicks'), prevent_initial_call=True)
def reset_values(n_clicks):
    if not n_clicks:
        raise dash.exceptions.PreventUpdate
    else:
        data = dff.to_dict('records')
        columns = display_columns
        
        return(data, columns)
        
@callback([Output('datatable', 'data', allow_duplicate=True),
           Output('datatable', 'columns', allow_duplicate=True)],
          [Input('rescue_options', 'value')], prevent_initial_call=True)
def filter_rescue_animals(option_chosen):
    
    if option_chosen == 'water':
        filtered_df = dff.loc[(df_filter.rescue_type.isin(['Water']))]
    
    elif option_chosen == 'mount/wild':
        filtered_df = dff.loc[(df_filter.rescue_type.isin(['Mountain/Wilderness']))]
        
    elif option_chosen == 'disast/ind':
        filtered_df = dff.loc[(df_filter.rescue_type.isin(['Disaster/Individual']))]
        
    elif option_chosen is None:
        data = dff.to_dict('records')
        columns=display_columns
    
    data = filtered_df.to_dict('records')
    columns = display_columns
    
    return (data, columns)

@callback([Output('datatable', 'data', allow_duplicate=True),
           Output('datatable', 'columns', allow_duplicate=True)],
          [Input('animal_types', 'value')], prevent_initial_call=True)
def filter_animal_type(option_chosen):
    
    if option_chosen == 'Dog':
        filtered_type = dff[dff['animal_type']=='Dog']
    
    elif option_chosen == 'Cat':
        filtered_type = dff[dff['animal_type']=='Cat']
        
    elif option_chosen == 'Other':
        filtered_type = dff[dff['animal_type']=='Other']
    
    elif option_chosen == 'Bird':
        filtered_type = dff[dff['animal_type']=='Bird']
        
    elif option_chosen == 'Livestock':
        filtered_type = dff[dff['animal_type']=='Livestock']
    
    elif option_chosen is None:
        data = dff.to_dict('records')
        columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in dff.columns]
    
    data = filtered_type.to_dict('records')
    columns = display_columns
    
    return (data, columns)

@callback(
    Output('graph-id','children'),
    Input('datatable', 'derived_viewport_data'))
def update_graphs(viewData):
    dff = pd.DataFrame.from_dict(viewData) # current data displayed
    names = dff['breed'].value_counts().keys()
    values = dff['breed'].value_counts().tolist()
    
    return [
        dcc.Graph(
            figure = px.pie(
            data_frame=dff,
            values = values, 
            names = names, 
            color_discrete_sequence=px.colors.sequential.RdBu,
            width=800,
            height=500)
        )
    ]

@callback(Output('map-id', 'children'),
          [Input('datatable', 'derived_virtual_data'),
           Input('datatable', 'derived_virtual_selected_rows'),
           Input('datatable', 'selected_columns')])
def update_map(viewData, selected_rows, selected_columns):
    dff = pd.DataFrame.from_dict(viewData)
    
    if selected_rows == []:
        selected_rows = [0]
        
    return [
        dl.Map(
            style={'width': '1000px', 'height': '500px'},
            center=[30.75, -97.48],
            zoom=6,
            children=[
                dl.TileLayer(id='base-layer-id'),
                dl.Marker(
                    position=[(dff.iloc[selected_rows[0], 13]), (dff.iloc[selected_rows[0], 14])],
                    children=[
                        dl.Tooltip(dff.iloc[selected_rows[0], 4]),
                        dl.Popup([
                            html.H5('Type: %s' % (dff.iloc[selected_rows[0], 3]), style={'color': 'Black'}),
                            html.H5('Name: %s' % (dff.iloc[selected_rows[0], 9]), style={'color': 'Black'}),
                            html.H5('Sex: %s' % (dff.iloc[selected_rows[0], 12]), style={'color': 'Black'}),
                            html.H5('Breed: %s' % (dff.iloc[selected_rows[0], 4]), style={'color': 'Black'}),
                            html.H5('Age: %s weeks' % (dff.iloc[selected_rows[0], 15].round(0)), style={'color': 'Black'}),
                            ])
                        ]
                    )
                ]
            )
        ]