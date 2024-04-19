import plotly.express as px
import plotly.graph_objs as go  

import pandas as pd

def update_film_graph(n_clicks, selected_films, df):
    if selected_films:
        filtered_df = df[df['Film'].isin(selected_films)]
        fig = px.bar(filtered_df, x='Year', y='Box office gross Worldwide', color='Film', barmode='group', title='Recettes mondiales au box-office pour les films sélectionnés')
        return fig
    else:
        return go.Figure()
