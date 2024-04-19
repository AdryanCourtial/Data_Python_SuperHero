import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Output, Input
import plotly.express as px

def update_main_graph(hover_data, df):
    if hover_data and 'points' in hover_data[0]:
        year = hover_data[0]['points'][0]['x']
        filtered_df = df[df['Year'] == year]
        fig = px.scatter(filtered_df, x='Budget', y='Box office gross Worldwide', color='Film', title=f'Recettes mondiales au box-office par rapport au budget en {year}')
        return fig
    else:
        return px.scatter(df, x='Budget', y='Box office gross Worldwide', color='Film', title='Recettes mondiales au box-office par rapport au budget')
