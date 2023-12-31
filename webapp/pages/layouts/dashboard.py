from dash import html
from webapp.pages.components.dash_table import data_table
from webapp.pages.components.radio import animal_types_radio, rescue_dog_radio
from webapp.pages.components.buttons import reset_button

DASHBOARD = html.Div(
    [
        html.Div(id='hidden-div', style={'display':'none'}),
        html.Div(className='row',style={'display' : 'flex'},
                 children=[
                     html.Div(className='col s12 m4',
                              children=[html.H5('Filter by Animal Type'),animal_types_radio]
                              ),
                     html.Div(className='col s12 m4',
                              children=[html.H5('Filter by Rescue Dog Type'),rescue_dog_radio,]
                              ),
                     html.Div(className='col s12 m4', 
                              style={
                                  'display': 'flex',
                                  'justify-content': 'center'
                                  }, children=reset_button)
                     ]),
        html.Hr(),
        html.Div(className='sticky-top',
                 children=data_table),
        html.Br(),
        html.Hr(),
        html.Div(
            className='row',
            style={'display' : 'flex'},
            children=[
                html.Div(
                    id='graph-id',
                    className='col s12 m6'
                    ),
                html.Div(
                    id='map-id',
                    className='col s12 m6'
                    )
                ]
            )
        ]
)