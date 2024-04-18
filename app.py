from dash import Dash, html, page_container
import pandas as pd

df = pd.read_csv('data/DATA_ESSAiE2.csv', delimiter=';')

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css', "https://fonts.googleapis.com/css2?family=M+PLUS+1+Code:wght@100..700&display=swap"]
app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True,  external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.Div(
            className="visite-bar",
            children= [
                html.Div(
                    className="logo",
                    children= [
                        html.A(
                            html.Img(className="logo",src='/assets/avengers-logo.png',alt="Je suis Le Logo du site"),
                            href='/'
                        )
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


