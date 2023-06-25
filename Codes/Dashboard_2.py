import dash
from flask import Flask
from plotly import express as px
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

#initiate the App
server = Flask(__name__)
app = dash.Dash(__name__, server = server, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

#Read the File
df = pd.read_csv('Ab_NYC__CLEANED.csv')
df['last_review']=pd.to_datetime(df['last_review'])
#Build Compomnent
Header= html.H1("Airbnb Visualizations Dashboard" , style={'color':'darkcyan', 'textAlign':'center'})

#Visuals
fig= go.FigureWidget()

fig.add_scatter(name="price", x=df["last_review"], y= df["price"], fill = "tonexty")
fig.add_scatter(name="number_of_reviews", x=df["last_review"], y= df["number_of_reviews"], fill = "tonexty")
fig.update_layout(title= "Room Prices and Reviews")

#Design the Layout
app.layout= html.Div(
[
        dbc.Row([Header]),
        dbc.Row([dbc.Col([dcc.Graph(figure=fig)]),dbc.Col()]),
    ]
)
#Run the App
app.run_server(debug=True)