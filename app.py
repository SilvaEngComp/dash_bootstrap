from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html

heart_disease = fetch_ucirepo(id=45)

dados = heart_disease.data.features
figura_histograma = px.histogram(data_frame=dados, x="age", title="Histograma de Idades").show()

dados["doenca"] = (heart_disease.data.targets > 0)*1
figura_boxplot  = px.box(dados, x="doenca", y="age", color='doenca', title='Boxplot de idades').show()
app = Dash(__name__)

div_histograma = html.Div([
           html.H1('Histograma de Idades'),

    dcc.Graph(figure=figura_boxplot) 
    ])
 
div_boxplot = html.Div([
               html.H1('Boxplot de idades'),

    dcc.Graph(figure=figura_boxplot)]),

app.layout = html.Div([
     html.H1('Análise de dados do UCI Repository Heart Disease'),
     div_histograma,
     div_boxplot,
    ])

app.run_server(debug=True)