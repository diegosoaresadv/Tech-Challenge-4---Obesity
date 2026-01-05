# -*- coding: utf-8 -*-
"""
Dashboard Interativo de Análise de Obesidade
Desenvolvido para análise médica de dados de obesidade
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

# ============================================================================
# CARREGAMENTO E PREPARAÇÃO DOS DADOS
# ============================================================================

# Carregar o dataset
df = pd.read_csv('data/Obesity_Tratado.csv')

# Criar IMC (Índice de Massa Corporal) como nova variável
df['IMC'] = df['Weight'] / (df['Height'] ** 2)
df['IMC'] = df['IMC'].round(2)

# Definir faixas etárias
df['Faixa_Etaria'] = pd.cut(df['Age'], 
                             bins=[0, 25, 35, 45, 100], 
                             labels=['18-25', '26-35', '36-45', '46+'])

# Tradução e organização das variáveis
traducao_variaveis = {
    'Gender': 'Sexo',
    'Age': 'Idade',
    'Height': 'Altura (m)',
    'Weight': 'Peso (kg)',
    'IMC': 'IMC',
    'family_history': 'Histórico Familiar',
    'FAVC': 'Consome Alimentos Calóricos',
    'FCVC': 'Freq. Consumo Vegetais',
    'NCP': 'Nº Refeições Principais',
    'CAEC': 'Consumo Entre Refeições',
    'SMOKE': 'Fumante',
    'CH2O': 'Consumo Diário Água',
    'SCC': 'Monitora Calorias',
    'FAF': 'Freq. Atividade Física',
    'TUE': 'Tempo Uso Tecnologia',
    'CALC': 'Consumo Álcool',
    'MTRANS': 'Meio Transporte',
    'Obesity': 'Nível de Obesidade'
}

# Ordenar níveis de obesidade
ordem_obesidade = [
    'Insufficient_Weight',
    'Normal_Weight',
    'Overweight_Level_I',
    'Overweight_Level_II',
    'Obesity_Type_I',
    'Obesity_Type_II',
    'Obesity_Type_III'
]

# Tradução dos níveis de obesidade
traducao_obesidade = {
    'Insufficient_Weight': 'Peso Insuficiente',
    'Normal_Weight': 'Peso Normal',
    'Overweight_Level_I': 'Sobrepeso Nível I',
    'Overweight_Level_II': 'Sobrepeso Nível II',
    'Obesity_Type_I': 'Obesidade Tipo I',
    'Obesity_Type_II': 'Obesidade Tipo II',
    'Obesity_Type_III': 'Obesidade Tipo III'
}

# ============================================================================
# CONFIGURAÇÃO DO APLICATIVO DASH
# ============================================================================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Cores do tema médico
CORES = {
    'primaria': '#2C3E50',
    'secundaria': '#3498DB',
    'sucesso': '#27AE60',
    'alerta': '#E74C3C',
    'fundo': '#ECF0F1',
    'texto': '#2C3E50'
}

# ============================================================================
# LAYOUT DO DASHBOARD
# ============================================================================

app.layout = dbc.Container([
    # Cabeçalho
    dbc.Row([
        dbc.Col([
            html.H1("📊 Dashboard de Análise de Obesidade", 
                   className="text-center mb-4",
                   style={'color': CORES['primaria'], 'fontWeight': 'bold'}),
            html.Hr(),
        ], width=12)
    ]),
    
    # Painel de Filtros
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("🔍 Filtros de Análise", className="text-white"),
                             style={'backgroundColor': CORES['primaria']}),
                dbc.CardBody([
                    # Filtro de Sexo
                    html.Label("Sexo:", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='filtro-sexo',
                        options=[{'label': 'Todos', 'value': 'Todos'}] + 
                               [{'label': x, 'value': x} for x in df['Gender'].unique()],
                        value='Todos',
                        clearable=False
                    ),
                    html.Br(),
                    
                    # Filtro de Faixa Etária
                    html.Label("Faixa Etária:", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='filtro-idade',
                        options=[{'label': 'Todas', 'value': 'Todas'}] + 
                               [{'label': x, 'value': x} for x in df['Faixa_Etaria'].unique()],
                        value='Todas',
                        clearable=False
                    ),
                    html.Br(),
                    
                    # Filtro de Nível de Obesidade
                    html.Label("Nível de Obesidade:", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='filtro-obesidade',
                        options=[{'label': 'Todos', 'value': 'Todos'}] + 
                               [{'label': traducao_obesidade.get(x, x), 'value': x} 
                                for x in ordem_obesidade],
                        value='Todos',
                        clearable=False
                    ),
                    html.Br(),
                    
                    # Filtro de Histórico Familiar
                    html.Label("Histórico Familiar de Sobrepeso:", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='filtro-historico',
                        options=[
                            {'label': 'Todos', 'value': 'Todos'},
                            {'label': 'Sim', 'value': 'yes'},
                            {'label': 'Não', 'value': 'no'}
                        ],
                        value='Todos',
                        clearable=False
                    ),
                ])
            ], className="mb-4")
        ], width=3),
        
        # Cards de Estatísticas
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("Total de Pacientes", className="text-muted"),
                            html.H3(id='card-total', className="text-primary")
                        ])
                    ])
                ], width=3),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("IMC Médio", className="text-muted"),
                            html.H3(id='card-imc', className="text-success")
                        ])
                    ])
                ], width=3),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("Idade Média", className="text-muted"),
                            html.H3(id='card-idade', className="text-info")
                        ])
                    ])
                ], width=3),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("% Obesidade", className="text-muted"),
                            html.H3(id='card-obesidade', className="text-danger")
                        ])
                    ])
                ], width=3),
            ], className="mb-4"),
        ], width=9),
    ]),
    
    # Abas de Visualizações
    dbc.Row([
        dbc.Col([
            dcc.Tabs(id='tabs-analise', value='tab-distribuicao', children=[
                dcc.Tab(label='📊 Distribuições', value='tab-distribuicao'),
                dcc.Tab(label='🔄 Correlações', value='tab-correlacoes'),
                dcc.Tab(label='📈 Comparações', value='tab-comparacoes'),
                dcc.Tab(label='📋 Tabela de Dados', value='tab-tabela'),
            ]),
            html.Div(id='conteudo-tabs')
        ], width=12)
    ]),
    
], fluid=True, style={'backgroundColor': CORES['fundo'], 'padding': '20px'})

# ============================================================================
# CALLBACKS - INTERATIVIDADE
# ============================================================================

@app.callback(
    [Output('card-total', 'children'),
     Output('card-imc', 'children'),
     Output('card-idade', 'children'),
     Output('card-obesidade', 'children')],
    [Input('filtro-sexo', 'value'),
     Input('filtro-idade', 'value'),
     Input('filtro-obesidade', 'value'),
     Input('filtro-historico', 'value')]
)
def atualizar_cards(sexo, idade, obesidade, historico):
    """Atualiza os cards de estatísticas com base nos filtros"""
    df_filtrado = df.copy()
    
    # Aplicar filtros
    if sexo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Gender'] == sexo]
    if idade != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Faixa_Etaria'] == idade]
    if obesidade != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Obesity'] == obesidade]
    if historico != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['family_history'] == historico]
    
    # Calcular estatísticas
    total = len(df_filtrado)
    imc_medio = df_filtrado['IMC'].mean()
    idade_media = df_filtrado['Age'].mean()
    
    # Calcular percentual de obesidade (tipos I, II, III)
    obesidade_count = df_filtrado[df_filtrado['Obesity'].str.contains('Obesity', na=False)].shape[0]
    perc_obesidade = (obesidade_count / total * 100) if total > 0 else 0
    
    return (
        f"{total:,}",
        f"{imc_medio:.2f}",
        f"{idade_media:.1f} anos",
        f"{perc_obesidade:.1f}%"
    )


@app.callback(
    Output('conteudo-tabs', 'children'),
    [Input('tabs-analise', 'value'),
     Input('filtro-sexo', 'value'),
     Input('filtro-idade', 'value'),
     Input('filtro-obesidade', 'value'),
     Input('filtro-historico', 'value')]
)
def renderizar_conteudo(tab, sexo, idade, obesidade, historico):
    """Renderiza o conteúdo de cada aba com base nos filtros"""
    df_filtrado = df.copy()
    
    # Aplicar filtros
    if sexo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Gender'] == sexo]
    if idade != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Faixa_Etaria'] == idade]
    if obesidade != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Obesity'] == obesidade]
    if historico != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['family_history'] == historico]
    
    if tab == 'tab-distribuicao':
        return criar_aba_distribuicao(df_filtrado)
    elif tab == 'tab-correlacoes':
        return criar_aba_correlacoes(df_filtrado)
    elif tab == 'tab-comparacoes':
        return criar_aba_comparacoes(df_filtrado)
    elif tab == 'tab-tabela':
        return criar_aba_tabela(df_filtrado)


def criar_aba_distribuicao(df_filtrado):
    """Cria visualizações de distribuição dos dados"""
    
    # Gráfico 1: Distribuição por Nível de Obesidade
    df_obesidade = df_filtrado['Obesity'].value_counts().reset_index()
    df_obesidade.columns = ['Obesity', 'count']
    df_obesidade['Obesity_Trad'] = df_obesidade['Obesity'].map(traducao_obesidade)
    
    fig1 = px.bar(df_obesidade, 
                  x='Obesity_Trad', 
                  y='count',
                  title='Distribuição por Nível de Obesidade',
                  labels={'Obesity_Trad': 'Nível de Obesidade', 'count': 'Quantidade'},
                  color='count',
                  color_continuous_scale='Blues')
    fig1.update_layout(showlegend=False, height=400)
    
    # Gráfico 2: Distribuição de IMC por Sexo
    fig2 = px.box(df_filtrado, 
                  x='Gender', 
                  y='IMC',
                  color='Gender',
                  title='Distribuição de IMC por Sexo',
                  labels={'Gender': 'Sexo', 'IMC': 'IMC'})
    fig2.update_layout(height=400)
    
    # Gráfico 3: Distribuição de Idade
    fig3 = px.histogram(df_filtrado, 
                       x='Age',
                       nbins=30,
                       title='Distribuição de Idade dos Pacientes',
                       labels={'Age': 'Idade'},
                       color_discrete_sequence=['#3498DB'])
    fig3.update_layout(height=400)
    
    # Gráfico 4: Peso vs Altura por Obesidade
    fig4 = px.scatter(df_filtrado, 
                     x='Height', 
                     y='Weight',
                     color='Obesity',
                     title='Relação Peso x Altura por Nível de Obesidade',
                     labels={'Height': 'Altura (m)', 'Weight': 'Peso (kg)', 'Obesity': 'Obesidade'},
                     hover_data=['Age', 'Gender', 'IMC'])
    fig4.update_layout(height=400)
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig1)], width=6),
            dbc.Col([dcc.Graph(figure=fig2)], width=6),
        ]),
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig3)], width=6),
            dbc.Col([dcc.Graph(figure=fig4)], width=6),
        ]),
    ], fluid=True, className="mt-4")


def criar_aba_correlacoes(df_filtrado):
    """Cria visualizações de correlação entre variáveis"""
    
    # Matriz de correlação das variáveis numéricas
    variaveis_numericas = ['Age', 'Height', 'Weight', 'IMC', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    df_corr = df_filtrado[variaveis_numericas].corr()
    
    fig1 = px.imshow(df_corr,
                     labels=dict(color="Correlação"),
                     x=[traducao_variaveis.get(x, x) for x in df_corr.columns],
                     y=[traducao_variaveis.get(x, x) for x in df_corr.columns],
                     title='Matriz de Correlação das Variáveis Numéricas',
                     color_continuous_scale='RdBu_r',
                     aspect="auto")
    fig1.update_layout(height=500)
    
    # Gráfico de dispersão: IMC vs Atividade Física
    fig2 = px.scatter(df_filtrado, 
                     x='FAF', 
                     y='IMC',
                     color='Obesity',
                     size='Age',
                     title='IMC vs Frequência de Atividade Física',
                     labels={'FAF': 'Frequência de Atividade Física', 'IMC': 'IMC', 
                            'Obesity': 'Obesidade', 'Age': 'Idade'},
                     hover_data=['Gender', 'Weight'])
    fig2.update_layout(height=400)
    
    # IMC médio por categoria
    fig3 = go.Figure()
    
    categorias = ['FAVC', 'SMOKE', 'SCC', 'family_history']
    labels_cat = ['Consome Alimentos Calóricos', 'Fumante', 'Monitora Calorias', 'Histórico Familiar']
    
    for i, (cat, label) in enumerate(zip(categorias, labels_cat)):
        imc_por_cat = df_filtrado.groupby(cat)['IMC'].mean().reset_index()
        fig3.add_trace(go.Bar(
            name=label,
            x=imc_por_cat[cat],
            y=imc_por_cat['IMC'],
        ))
    
    fig3.update_layout(
        title='IMC Médio por Variáveis Categóricas',
        xaxis_title='Categoria',
        yaxis_title='IMC Médio',
        barmode='group',
        height=400
    )
    
    # Consumo de água vs IMC
    fig4 = px.box(df_filtrado, 
                  x='CH2O', 
                  y='IMC',
                  color='Gender',
                  title='Relação entre Consumo de Água e IMC',
                  labels={'CH2O': 'Consumo Diário de Água (L)', 'IMC': 'IMC', 'Gender': 'Sexo'})
    fig4.update_layout(height=400)
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig1)], width=12),
        ]),
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig2)], width=6),
            dbc.Col([dcc.Graph(figure=fig3)], width=6),
        ]),
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig4)], width=12),
        ]),
    ], fluid=True, className="mt-4")


def criar_aba_comparacoes(df_filtrado):
    """Cria visualizações comparativas"""
    
    # Comparação de hábitos alimentares por obesidade
    fig1 = px.violin(df_filtrado, 
                     y='Obesity', 
                     x='FCVC',
                     color='Gender',
                     title='Frequência de Consumo de Vegetais por Nível de Obesidade',
                     labels={'FCVC': 'Freq. Consumo de Vegetais', 'Obesity': 'Nível de Obesidade', 
                            'Gender': 'Sexo'})
    fig1.update_layout(height=500)
    
    # Atividade física por obesidade
    fig2 = px.box(df_filtrado, 
                  x='Obesity', 
                  y='FAF',
                  color='Obesity',
                  title='Atividade Física por Nível de Obesidade',
                  labels={'FAF': 'Frequência de Atividade Física', 'Obesity': 'Nível de Obesidade'})
    fig2.update_layout(height=400, showlegend=False)
    
    # Meio de transporte vs Obesidade
    df_trans = df_filtrado.groupby(['MTRANS', 'Obesity']).size().reset_index(name='count')
    fig3 = px.bar(df_trans, 
                  x='MTRANS', 
                  y='count',
                  color='Obesity',
                  title='Meio de Transporte vs Nível de Obesidade',
                  labels={'MTRANS': 'Meio de Transporte', 'count': 'Quantidade', 
                         'Obesity': 'Nível de Obesidade'},
                  barmode='group')
    fig3.update_layout(height=400)
    
    # Tempo de uso de tecnologia vs IMC
    fig4 = px.scatter(df_filtrado, 
                     x='TUE', 
                     y='IMC',
                     color='Obesity',
                     size='Age',
                     title='Tempo de Uso de Tecnologia vs IMC',
                     labels={'TUE': 'Tempo de Uso de Tecnologia (h)', 'IMC': 'IMC', 
                            'Obesity': 'Obesidade', 'Age': 'Idade'})
    fig4.update_layout(height=400)
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig1)], width=12),
        ]),
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig2)], width=6),
            dbc.Col([dcc.Graph(figure=fig3)], width=6),
        ]),
        dbc.Row([
            dbc.Col([dcc.Graph(figure=fig4)], width=12),
        ]),
    ], fluid=True, className="mt-4")


def criar_aba_tabela(df_filtrado):
    """Cria tabela interativa com os dados filtrados"""
    
    # Preparar dataframe para exibição
    df_display = df_filtrado[['Gender', 'Age', 'Height', 'Weight', 'IMC', 
                              'family_history', 'FAVC', 'FAF', 'Obesity']].copy()
    
    # Renomear colunas
    df_display.columns = ['Sexo', 'Idade', 'Altura', 'Peso', 'IMC', 
                         'Hist. Familiar', 'Alim. Calóricos', 'Ativ. Física', 'Obesidade']
    
    # Traduzir obesidade
    df_display['Obesidade'] = df_display['Obesidade'].map(traducao_obesidade)
    
    # Estatísticas resumidas
    stats = html.Div([
        html.H4("📊 Estatísticas Resumidas", className="mt-4 mb-3"),
        dbc.Row([
            dbc.Col([
                html.P([html.Strong("Total de registros: "), f"{len(df_display)}"]),
                html.P([html.Strong("IMC médio: "), f"{df_filtrado['IMC'].mean():.2f}"]),
                html.P([html.Strong("Idade média: "), f"{df_filtrado['Age'].mean():.1f} anos"]),
            ], width=4),
            dbc.Col([
                html.P([html.Strong("Peso médio: "), f"{df_filtrado['Weight'].mean():.1f} kg"]),
                html.P([html.Strong("Altura média: "), f"{df_filtrado['Height'].mean():.2f} m"]),
                html.P([html.Strong("Desvio padrão IMC: "), f"{df_filtrado['IMC'].std():.2f}"]),
            ], width=4),
            dbc.Col([
                html.P([html.Strong("% Sexo Feminino: "), 
                       f"{(df_filtrado['Gender']=='Female').sum()/len(df_filtrado)*100:.1f}%"]),
                html.P([html.Strong("% Histórico Familiar: "), 
                       f"{(df_filtrado['family_history']=='yes').sum()/len(df_filtrado)*100:.1f}%"]),
                html.P([html.Strong("Ativ. Física média: "), f"{df_filtrado['FAF'].mean():.2f}"]),
            ], width=4),
        ])
    ])
    
    # Tabela interativa
    tabela = dash_table.DataTable(
        data=df_display.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df_display.columns],
        page_size=15,
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '10px',
            'fontFamily': 'Arial'
        },
        style_header={
            'backgroundColor': CORES['primaria'],
            'color': 'white',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#F8F9FA'
            }
        ],
        sort_action="native",
        filter_action="native",
        export_format="xlsx",
        export_headers="display",
    )
    
    return dbc.Container([
        stats,
        html.Hr(),
        html.H4("📋 Dados Detalhados", className="mb-3"),
        html.P("Você pode ordenar, filtrar e exportar os dados abaixo:", 
               className="text-muted"),
        tabela
    ], fluid=True, className="mt-4")


# ============================================================================
# EXECUTAR APLICATIVO
# ============================================================================

if __name__ == '__main__':
    app.run(debug=True, port=8050)
