from dash import register_page, callback, dcc,  Output, Input, State
from dash import html
from dash import Dash, html, dcc, callback, Output, Input, State
from graph.film_graph import update_film_graph
from graph.comparison_graph import update_main_graph
from graph.critic_graph import update_critic_graph
from graph.pie_chart import create_pie_chart
import app

register_page(__name__, path='/')


# Layout
layout = html.Div(
    className="main_body",
    children=[
        html.Div(
            className="sidebar",
            children=[
                html.A("Contenue 1", href="#content-1"),
                html.A("Contenue 2"),
                html.A("Contenue 3"),
                html.A("Contenue 4"),
                html.A("Contenue 5"),
            ]
        ),
        html.Div(
            className="content",
            children=[
                html.Div(
                    children = [
                        html.H2("Recette Généré dans le monde entier (Brute)"),
                        html.Div(
                            id="content-1",
                            children= [
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
                ),
                html.Div(
                    id="content-2",
                    children = [
                        html.H2("Je suis le Cotent 2"),
                        html.Div([
                            dcc.Graph(id='comparison-graph')
                        ], className='container mt-5'),
                        html.P("""Je Suis le Deuxieme Content Super Interessante, Genre c'est 
                               improbable personne me lie""")
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

@callback(
    Output('comparison-graph', 'figure'),
    [Input('film-graph-content', 'hoverData')]
)
def update_comparison(hover_data):
    return update_main_graph(hover_data, app.df)

@callback(
    Output('critic-graph', 'figure'),
    [Input('update-film-button', 'n_clicks')]
)
def update_critic_graph_callback(n_clicks):
    return update_critic_graph(app.df)

@callback(
    Output('pie-chart-content', 'figure'),
    [Input('pie-chart-content', 'id')]
)
def display_pie_chart(id):
    return create_pie_chart(app.df)