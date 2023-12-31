from dash import html

reset_button = html.Button('RESET FILTERS',
                            id='reset-rescue-button', 
                            n_clicks=0,
                            style={
                                'background-color': '#04AA6D',
                                'color': 'White',
                                'text-align': 'center',
                                'font-size': '24px',
                                'border-radius': '8px',
                                'width': '250px',
                                'padding': '8px'
                                }
                            ),

