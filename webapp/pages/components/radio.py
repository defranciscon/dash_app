from dash import dcc, html
from webapp.pages.data.models import dff

animal_types_radio = dcc.RadioItems(
                            id='animal_types',
                            options=[
                                {
                                    'label': [
                                        html.Span(x, style={
                                            'font-size': 25, 
                                            'font-color': 'White',
                                            'padding-left': 15,
                                            'padding-right': 15
                                            })
                                        ],
                                    'value': x
                                    }
                                for x in dff['animal_type'].unique()
                                ],
                            labelStyle={'display': 'inline-block'}
                        )

rescue_dog_radio = dcc.RadioItems(
                            id='rescue_options',
                            options = [
                                {
                                    'label': [
                                        html.Span("Water", style= {
                                            'font-size': 25, 
                                            'font-color': 'White',
                                            'padding-left': 15,
                                            'padding-right': 15
                                            })
                                        ],
                                    'value': 'water'
                                    },
                                {
                                    'label': [
                                        html.Span("Mountain/Wilderness", style={
                                            'font-size': 25, 
                                            'font-color': 'White',
                                            'padding-left': 15,
                                            'padding-right': 15
                                            })
                                        ],
                                    'value': 'mount/wild'
                                    },
                                {
                                    'label': [
                                        html.Span("Disaster", style={
                                            'font-size': 25, 
                                            'font-color': 'White',
                                            'padding-left': 15,
                                            'padding-right': 15
                                            })
                                        ],
                                    'value': 'disast/ind'
                                    },
                                ],
                            labelStyle={'display': 'inline-block'}
                            )