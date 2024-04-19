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
                html.A("Contenue 2", href="#content-2"),
                html.A("Contenue 3", href="#content-3"),
                html.A("Contenue 4", href="#content-4"),
                
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
                        html.P("""graphique de dispersion  qui compare les recettes mondiales au box-office
                                par rapport au budget des films pour une année donnée. Si l'utilisateur survole le 
                               graphique et sélectionne une année spécifique, le graphique sera filtré pour afficher uniquement les films de cette année-là. 
                               Sinon, si aucune année n'est sélectionnée, le graphique montrera les données pour toutes les années disponibles""")
                    ]
                ),
                html.Div(
                    id="content-3",
                    children = [
                        html.H2("Je suis le Cotent 3"),
                        html.Div([
                            dcc.Graph(id='critic-graph')
                        ], className='container mt-5'),
                        html.P("""Ce graphique compare les scores moyens des critiques pour les films de Marvel et DC. Il montre
                                quelle franchise a généralement obtenu de meilleures 
                               critiques selon les données fournies. Les barres rouges représentent les scores moyens des films Marvel, 
                               tandis que les barres bleues représentent les scores moyens des films DC.""")
                    ]
                ),
                html.Div(
                    id="content-4",
                    children = [
                        html.H2("Je suis le Cotent 4"),
                        html.Div([
                            dcc.Graph(id='pie-chart-content', figure=create_pie_chart(app.df))
                            ], className='container mt-5'),
                        html.P("""Cette fonction crée un graphique en secteurs  qui illustre la répartition des recettes mondiales entre différentes franchises de films. Chaque secteur du graphique représente une franchise, et sa taille est proportionnelle à la part des recettes mondiales qu'elle a générée""")
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