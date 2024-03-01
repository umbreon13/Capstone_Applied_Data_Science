# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                    options=[{'label': 'All Sites', 'value': 'ALL'},
                                            {'label': 'Cape Canaveral Launch Complex 40 (CCAFS LC-40)', 'value': 'CCAFS LC-40'},
                                            {'label': 'Cape Canaveral Space Launch Complex 40 (CCAFS SLC-40)', 'value': 'CCAFS SLC-40'},
                                            {'label': 'Kennedy Space Center Launch Complex 39A (KSC LC-39A)', 'value': 'KSC LC-39A'},
                                            {'label': 'Vandenberg Space Launch Complex 4 (VAFB SLC-4E)', 'value': 'VAFB SLC-4E'}],
                                    value='ALL',
                                    placeholder='All launch sites',
                                    searchable=True,  #we can enter keywords to search sites
                                    style={'width':'80%', 'padding': '3px', 'textAlign': 'center', 'color': '#503D36', 'font-size': 20}),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                value=[min_payload, max_payload],
                                                marks={0: '0 kg',
                                                        2500: '2500',
                                                        5000: '5000',
                                                        7500: '7500',
                                                        10000: '10000'}
                                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown',component_property='value'))

def get_pie_chart(entered_site):
    
    filtered_df = spacex_df
    if entered_site == 'ALL':
        filtered_df = spacex_df[spacex_df['class'] == 1].groupby('Launch Site').size().reset_index(name='Success_cases')
        fig = px.pie(filtered_df, values='Success_cases', 
        names='Launch Site', 
        title='Proportion of successful launches per location',
        )
        
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site].groupby('class').size().reset_index(name='Class_count')
        fig = px.pie(filtered_df,
        values='Class_count',
        names='class',
        title=f"Proportion of successful launches in {entered_site}",
        )

    return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'), 
     Input(component_id="payload-slider", component_property="value")]
     )

def get_scatter(site, PL_range):
    df = spacex_df
    low, high = PL_range

    if site == 'ALL':
        df = df[['class','Payload Mass (kg)','Booster Version Category']]

    else:
        df = df[df['Launch Site'] == site]
        df = df[['class','Payload Mass (kg)','Booster Version Category']]

    df_filtered = df[(df['Payload Mass (kg)'] >= low) & (df['Payload Mass (kg)'] <= high)]
    fig = px.scatter(df_filtered, x="Payload Mass (kg)", y="class", 
                    color="Booster Version Category",
                    title='Success rate per PL and Booster version'
                    )
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server()
