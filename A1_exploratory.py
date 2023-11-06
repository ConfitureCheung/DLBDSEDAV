import pandas as pd
import numpy as np
import os
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output


# plotly
df_concat = pd.read_csv('df_concat.csv')

print(df_concat['Region'].unique())

# region list
asia_r_list = ["Southern Asia", "Southeastern Asia", "Eastern Asia"]
europe_r_list = ["Central and Eastern Europe", "Western Europe", "Southeast Europe"]
africa_r_list = ["Middle East and Northern Africa", "Sub-Saharan Africa", "Southeast Africa",
                 "Horn of Africa", "Eastern Central Africa", "Western Africa"]
n_america_r_list = ["North America", "Central America"]
s_america_r_list = ["Latin America and Caribbean"]
oceania_r_list = ["Australia and New Zealand"]
continent_lists = [asia_r_list, europe_r_list, africa_r_list, n_america_r_list, s_america_r_list, oceania_r_list]
yr_list = list(range(2015, 2023, 1))


''' Australia and New Zealand is not shown in submap '''
# SCATTERGEO IN DASH
app = Dash(__name__)

app.layout = html.Div([
    html.H2('World Happiness Ranking from 2015 to 2022'),
    html.P('Year:'),
    html.Div([dcc.Slider(id='slider', min=2015, max=2022, step=1, value=2015,
                         marks={x: str(x) for x in list(range(2015, 2023, 1))})],
             style={'width': '75%', 'margin': 25, 'textAlign': 'center'}),
    dcc.Graph(id="graph"),
    html.P('Continent:'),
    html.Div([dcc.RadioItems(id='radio_btn',
                             options=['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania'],
                             value='Asia', inline=True)]),

    dcc.Graph(id="graph_barchart"),

    html.P('Rank Range:'),
    html.Div([dcc.Slider(id='slider_rank', min=10, max=160, step=10, value=10,
                         marks={x: str(x) for x in list(range(10, 161, 10))})],
             style={'width': '75%', 'margin': 25, 'textAlign': 'center'}),
    dcc.Graph(id="graph_linegraph"),

    dcc.Graph(id="graph_boxplot"),

    html.Div(children=[
            dcc.Graph(id="graph_asia", style={'display': 'inline-block'}),
            dcc.Graph(id="graph_europe", style={'display': 'inline-block'}),
            dcc.Graph(id="graph_africa", style={'display': 'inline-block'}),
            dcc.Graph(id="graph_n_america", style={'display': 'inline-block'}),
            dcc.Graph(id="graph_s_america", style={'display': 'inline-block'}),
        ])
])


def create_submaps(submap, output_graph, title, colorbar, h, w, geo_name=None, region_list=None):
    @app.callback(
        Output(output_graph, "figure"),
        Input('slider', 'value'))
    def plotly_map(yr):
        if submap:
            df = df_concat.query(f'Year == {yr} & Region in {region_list}')
        else:
            df = df_concat.query(f'Year == {yr}')

        geometry = gpd.points_from_xy(df.Longitude, df.Latitude)

        geo_df = gpd.GeoDataFrame(
            df[['Year', 'Country', 'Region', 'Latitude', 'Longitude', 'Rank', 'Size']], geometry=geometry
        )

        fig = go.Figure(data=go.Scattergeo(
            lon=geo_df.geometry.x,
            lat=geo_df.geometry.y,
            text=df[["Country", "Rank"]],
            mode='markers',
            marker=dict(
                size=geo_df['Size'],
                opacity=0.8,
                reversescale=True,
                autocolorscale=False,
                symbol='circle',
                line=dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                ),
                colorscale='Inferno',
                cmin=0,
                color=geo_df['Rank'],
                cmax=geo_df['Rank'].max(),
                colorbar_title=colorbar,
            )))

        fig.update_layout(height=h, width=w)
        fig.update_layout({
            'title': {
                'text': f'<b>{title} - Year {yr}</b>',
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': {'size': 18},
            }
        })
        # scale down to continent
        # "africa" | "asia" | "europe" | "north america" | "south america" | "usa" | "world"
        if submap:
            fig.update_layout(
                geo_scope=geo_name,
            )

        return fig


create_submaps(submap=False, output_graph='graph', title='Worldwide', colorbar="Ranking", h=700, w=1500)
create_submaps(submap=True, output_graph='graph_asia', title='Asia', colorbar=None, h=450, w=600, geo_name='asia',
               region_list=asia_r_list)
create_submaps(submap=True, output_graph='graph_europe', title='Europe', colorbar=None, h=450, w=600, geo_name='europe',
               region_list=europe_r_list)
create_submaps(submap=True, output_graph='graph_africa', title='Africa', colorbar=None, h=450, w=600, geo_name='africa',
               region_list=africa_r_list)
create_submaps(submap=True, output_graph='graph_n_america', title='North America', colorbar=None, h=450, w=600,
               geo_name='north america', region_list=n_america_r_list)
create_submaps(submap=True, output_graph='graph_s_america', title='South America', colorbar=None, h=450, w=600,
               geo_name='south america', region_list=s_america_r_list)


@app.callback(
        Output("graph_boxplot", "figure"),
        Input('slider', 'value'))
def plotly_boxplot(yr):
    df = df_concat.query(f'Year == {yr}')
    fig = px.box(df, x='Continent', y='Rank', hover_data=df.columns)
    fig.update_layout(height=700, width=1500)
    fig.update_layout({
        'title': {
            'text': f'<b>Boxplot Rank by Continent - Year {yr}</b>',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 18},
        }
    })

    return fig


@app.callback(
        Output("graph_linegraph", "figure"),
        Input('slider', 'value'),
        Input('slider_rank', 'value'))
def plotly_linegraph(yr, rank):
    # df = df_concat.query('Rank <= 10')
    df = df_concat.query(f'{rank - 10} <= Rank <= {rank}')
    fig = px.line(df, x="Year", y="Rank", color='Country', title=f'Happiness Ranking of Countries')
    fig.add_vline(x=yr, line_width=3, line_dash="dash", line_color="green")

    return fig


@app.callback(
        Output("graph_barchart", "figure"),
        Input('slider', 'value'),
        Input('radio_btn', 'value'))
def plotly_barchart(yr, region):
    df = df_concat.query(f'Continent == "{region}" & Year == {yr}')
    categories = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom',
                  'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']

    fig = go.Figure(data=[
        go.Bar(name=categories[0], x=df['Country'], y=df[categories[0]]),
        go.Bar(name=categories[1], x=df['Country'], y=df[categories[1]]),
        go.Bar(name=categories[2], x=df['Country'], y=df[categories[2]]),
        go.Bar(name=categories[3], x=df['Country'], y=df[categories[3]]),
        go.Bar(name=categories[4], x=df['Country'], y=df[categories[4]]),
        go.Bar(name=categories[5], x=df['Country'], y=df[categories[5]]),
        go.Bar(name=categories[6], x=df['Country'], y=df[categories[6]])
    ])
    fig.update_layout(title=f"Factors of happiness Score in {region}, Year {yr}")

    return fig


app.run_server(debug=True)




