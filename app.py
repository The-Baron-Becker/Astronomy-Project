import dash 
#import dash_core_components as dcc
from dash import dcc
from dash.dash import Dash
import dash_html_components as html
#from dash_html_components.Div import Div
from numpy.lib.arraypad import pad
import plotly.graph_objects as go
import plotly.express as px
import dash_table
import pandas as pd 
import colorlover as cl
from dash.dependencies import Input, Output
import numpy as np
import csv
import dash_auth
from dash import dash_table
from dash import html
import dash_table.FormatTemplate as FormatTemplate
from functions import *       
import base64



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

VALID_USERNAME_PASSWORD_PAIRS = {
    ' ': ' '
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "STARFINDER"
server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

df = pd.DataFrame([])

def build_banner():
    return dcc.Markdown('''
    ### *STARFINDER* ✨ BETA
        ''')


def build_bannar2():
    return dcc.Markdown('''
    *** 1.*** please choose the ***file*** you would like to identify stars in.
        ''')

def build_intro():
    return dcc.Markdown('''
    Welcome to starfinder
    ''')



def build_dropdown():

    return html.Div([
        dcc.Dropdown(
        id = 'dropdown',
        options=[
        {'label': 'Image 1', 'value': 'file1'},
        {'label': 'Image 2', 'value': 'file2',},
        {'label': 'Image 3', 'value': 'file3'},
        {'label': 'Image 4', 'value': 'file4'},
        {'label': 'Image 5', 'value': 'file5'}
        ],
        multi=True,
        value="MTL")])


def build_button():
    return html.Button(
        'GO', id = 'button')


app.layout = html.Div(
    #id = 'body',
    style={
        'margin-left': 80,
        'margin-right': 80,
        'margin-top': 80,
        'margin-bottom': 80
    },
    id="body",
    children=[

        html.Div(
            build_banner(),
        ),

        dcc.Tabs([
        dcc.Tab(label='Home', children=[

            build_intro()

        ]),
        dcc.Tab(label='Catalogue', children=[
            #build_bannar1(),
            #build_session_select(),
            build_bannar2(),
            html.Div([build_dropdown(), build_button()]),
            html.Div(id='dd-output-container')
        ]
        )
        ]
        )
    ]
)

@app.callback(dash.dependencies.Output('dd-output-container', 'children'),
			 [dash.dependencies.Input('button', 'n_clicks'),
             #dash.dependencies.Input('session_dropdown', 'value'),
             dash.dependencies.Input('dropdown', 'value')])

def update_output(n_clicks, image):
    if n_clicks is not None:
        image = image[0]
        image = find_stars(image)
        encoded_image = base64.b64encode(open(image, 'rb').read())
        return html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image))
])

if __name__ == '__main__':
    app.run_server(debug=True)