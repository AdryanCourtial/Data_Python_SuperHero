from dash import register_page
from dash import html

register_page(__name__, path='/')

layout = html.Div(
    className="sidebar",
    children= [
        html.A("Contenue 1"),
        html.A("Contenue 2"),
        html.A("Contenue 3"), 
        html.A("Contenue 4"),
        html.A("Contenue 4"),
    ]
)