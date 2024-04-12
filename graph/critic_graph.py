import pandas as pd
import plotly.express as px

def update_critic_graph(df):
    marvel_total_score = df[df['Franchise'] == 'Marvel']['Rotten Tomatoes Critic Score'].mean()
    dc_total_score = df[df['Franchise'] == 'DC']['Rotten Tomatoes Critic Score'].mean()

    data = {'Franchise': ['Marvel', 'DC'], 'Total Critic Score': [marvel_total_score, dc_total_score]}
    df_total_score = pd.DataFrame(data)

    fig = px.bar(df_total_score, x='Franchise', y='Total Critic Score', 
                 title='Total Critic Scores between Marvel and DC Films',
                 text='Total Critic Score', 
                 color='Franchise',
                 color_discrete_map={'Marvel': 'red', 'DC': 'blue'} 
                )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside') 
    fig.update_layout(height=550, width=800) 
    return fig
