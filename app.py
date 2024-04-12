from dash import Dash, html, page_container

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div(
    children=[
        html.Div(
            className="visite-bar",
            children= [
                html.Div(
                    className="logo",
                    children= [
                        html.Span('MonSuperSite'),
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
if __name__ == '__main__':
    app.run_server(debug=True)


