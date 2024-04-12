from dash import Dash, html, Output, Input, State, page_container
import pandas as pd

df = pd.read_csv('data/DATA_ESSAiE2.csv', delimiter=';')

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div(
    children=[
        html.Div(
            className="visite-bar",
            children= [
                html.Div(
                    className="logo",
                    children= [
                        html.A('MonSuperSite', href='/'),
                    ]
                ),
                html.Div(
                    className="nav-links",
                    children= [
                        html.A('À propos', href='/about'),
                        html.A('Contact', href='/contact'),
                    ]
                ),
        ]),
        page_container
    ]
)

app.run_server(port=8051, debug=True)


