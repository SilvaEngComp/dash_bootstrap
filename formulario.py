"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""

import dash_bootstrap_components as dbc
from dash import Dash,Input, Output, dcc, html
from dash.dependencies import Input, Output,State

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

page_home = html.Div([
    dbc.Row(dbc.Col(html.H1('Cálculo dos meses da idade')),justify="start"),
    dbc.Row(
        [ 
         dbc.Col(dbc.Label('Idade:'),width=1),
         dbc.Col(dbc.Input(id="idade",  type='number', placeholder="Digite a idade..."),width=8),
     dbc.Col(dbc.Button('Enviar', id='send-button', n_clicks=0),width=1),
             
        ],justify="start"
    ),
    
   html.Br(),
    dbc.Row(dbc.Col(dbc.Alert(id="output-monthes")),align='center',justify="end")
])

@app.callback(
    output = Output('output-monthes','children'),
    state = State('idade','value'),
    inputs = Input('send-button','n_clicks'),
    prevent_initial_call=True

)
def calcula_meses(n_clicks,idade):
    if n_clicks ==0 or idade is None:
        return ''
    return idade*12

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return page_home
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)