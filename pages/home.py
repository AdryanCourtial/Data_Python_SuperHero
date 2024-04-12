from dash import register_page, callback, dcc,  Output, Input, State
from dash import html
from graph.film_graph import update_film_graph
import app

register_page(__name__, path='/')


# Layout
layout = html.Div(
    children=[
        html.Div(
            className="sidebar",
            children=[
                html.A("Contenue 1"),
                html.A("Contenue 2"),
                html.A("Contenue 3"),
                html.A("Contenue 4"),
                html.A("Contenue 5"),
            ]
        ),
        html.Div(
            className="all_content",
            children=[
                html.Div(
                    className="reel_body",
                    children = [
                        html.H2("Recette Généré dans le monde entier (Brute)"),
                        html.Div([
                            html.H1(children='Analyse des données', className='text-center mb-4'),
                            html.Div([
                                dcc.Dropdown(
                                    options=[{'label': film, 'value': film} for film in app.df['Film']],
                                    value=[app.df['Film'][0]],
                                    multi=True,
                                    id='film-dropdown',
                                    className='form-control'
                                ),
                                html.Button('Update Film Graph', id='update-film-button', className='btn btn-primary mt-2')
                            ], className='form-group'),
                            dcc.Graph(id='film-graph-content')
                        ], className='container mt-5'),
                        html.P("""Je suis La description de fou mec c'est incroyable
                                comment baptiste est beau et genre personne le remarque""")
                    ]
                )
            ]
        )
    ]
)


@callback(
    Output('film-graph-content', 'figure'),
    [Input('update-film-button', 'n_clicks')],
    [State('film-dropdown', 'value')]
)
def update_film(n_clicks, selected_films):
    return update_film_graph(n_clicks, selected_films, app.df)