import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Output

def create_pie_chart(df):
    total_gross_by_franchise = df.groupby('Franchise')['Box office gross Worldwide'].sum().reset_index()

    fig = px.pie(total_gross_by_franchise, 
                 values='Box office gross Worldwide', 
                 names='Franchise')

    return fig
