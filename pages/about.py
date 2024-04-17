from dash import register_page
from dash import html
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, State
from graph.film_graph import update_film_graph
from graph.comparison_graph import update_main_graph
from graph.critic_graph import update_critic_graph
from graph.pie_chart import create_pie_chart


register_page(__name__)


df = pd.read_csv('data/DATA_ESSAiE2.csv', delimiter=';')

app = Dash(__name__)

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    
])