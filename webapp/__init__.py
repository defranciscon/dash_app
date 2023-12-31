import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from pymongo import MongoClient
from urllib.parse import quote_plus
from webapp.pages.layouts.navbar import NAVBAR
from webapp.pages.layouts.header import DASHBOARD_HEADER

host = '127.0.0.1'
db = quote_plus('AAC')
uri = 'mongodb://%s' % (host)
client = MongoClient(uri)

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div(
    [
        NAVBAR,
        DASHBOARD_HEADER,
        dash.page_container
        ],
    )


