import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def main():
    st.set_page_config(page_title='Obras', layout='wide', initial_sidebar_state='collapsed')

    # Estilos de Texto ---------------------------------------
    st.markdown("""
               <style>
                   .boxed {
                       border: 2px solid #428bca;
                       border-radius: 5px;
                       padding: 5px;
                       font-size: 70px;
                       font-weight: bold;
                       font-family: 'Helvetica', sans-serif;
                   }
               </style>
           """, unsafe_allow_html=True)

    st.markdown("""
                   <style>
                       .title {
                           border: 2px solid #428bca;
                           border-radius: 5px;
                           padding: 5px;
                           font-size: 48px;
                           font-weight: bold;
                           font-family: 'Helvetica', sans-serif;
                       }
                   </style>
               """, unsafe_allow_html=True)

    st.markdown("""
                   <style>
                       .fields {
                           font-size: 30px;
                           text-align: left;
                       }
                   </style>
               """, unsafe_allow_html=True)

    #Sidebar --------------------------------------------------------
    sidebar = st.sidebar
    sidebar.title('FILTROS')
    d = sidebar.date_input("Selecione a data de visualização", datetime.date(2019, 7, 6))
    Empresa = sidebar.selectbox("Qual a Empresa?", ('Empresa 1', 'Empresa 2') )
    Outro_Filtro = sidebar.selectbox("Qual Outro Filtro?", ('Outro 1', 'Outro2 2'))

    # Visual-----------------------------------------------------------------------
    col1, col2 = st.columns([4, 3])

    # Adicione o título dentro da caixa
    col1.markdown('<p class="boxed">{}</p>'.format('Página de Obras'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('SELECIONE A OBRA'), unsafe_allow_html=True)
    select_obra = col1.selectbox('obra', ('Obra 1', 'Obra 2', 'Obra 3'), label_visibility='collapsed')
    selectvisao = col1.selectbox('Qual visão deseja ver', ('Real', 'Projetado', 'Projetado Atualizado', 'Simulado'))

    st.divider()

    col1,col2 = st.columns([4,3])
    col1.markdown('<p class="title">{}</p>'.format('Informações Gerais'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Gerar Arquivo'), unsafe_allow_html=True)

    col1, col2 = st.columns([3,3])
    col1.markdown('<p class="fields">{}</p>'.format('ID: 51351813'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Nome: Obra do Meia Ponte'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Data de Início: 12/01/2023'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Previsão (Meses): 30'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Duração: 15/30'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('% Completo: 50%'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Qtd. MOD1: 120'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Qtd. MOD2: 150'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Orçamento MOD1: R$ 150.000,00'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Orçamento MOD2: R$ 300.000,00'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Contrato MOD1: R$ 170.000,00'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Contrato MOD2: R$ 330.000,00'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('R$ Venda MOD1: R$ 330.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('R$ Venda MOD2: R$ 580.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('% Permuta: 12%'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Tx Adm: R$ 150,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Total M²: 3.000.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Área Total/Apt.: 300'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Custo/Apt: R$ 150.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Custo M²: R$ 5000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format(''), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Receita Projetada: R$ 50.000.000,00'), unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns([4, 6, 1])

    col1.markdown('<p class="title">{}</p>'.format('Vendas'), unsafe_allow_html=True)
    col1.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)

    linha1 = ['Projetado', '15000', '20000', '30000', '1000', '50000', '15000', '20000', '30000', '1000', '50000']
    linha2 = ['Realizado', '300', '500', '404', '100', '500', '300', '500', '400', '100', '500']
    linha3 = ['Ajustado', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000']
    linha4 = ['Simulado', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000',
              '10000']

    array_fluxo_caixa = np.array([linha1, linha2, linha3, linha4])
    df_fluxo = pd.DataFrame(array_fluxo_caixa, columns=['Visão', 'Mês1', 'Mês2', 'Mês3', 'Mês4', 'Mês5', 'Mês6',
                                                        'Mês7', 'Mês8', 'Mês9', 'Mês10'])
    col1.dataframe(df_fluxo, hide_index=True)

    select_2 = col2.selectbox('Qual visão deseja ver?', ('Projetado', 'Realizado', 'Ajustado','Simulado'))
    # Dados do gráfico de linha
    x_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_line = [161,1561,1561,158,822,898,9253,18,9654,56,98,8411]

    # Dados do gráfico de barras (eixo secundário)
    x_bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_bar = [4000, 13000, 50000, 15000, 12000, 70000, 59000, 89000, 40000, 125500, 15000, 84000]

    # Criar o gráfico principal de linha
    fig = make_subplots(specs=[[{'secondary_y': True}]])

    fig.add_trace(go.Bar(x=x_bar, y=y_bar, name='Outra Métrica', opacity=0.5), secondary_y=True)
    fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines+markers', name='Série Temporal'))

    fig.update_traces(hovertemplate='%{y:.2f}%<br>%{x}')
    fig.update_layout(
        xaxis_title='Mês',
        title='Série Temporal com Eixo Secundário',
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            orientation="h",
        )
    )

    # Exibir o gráfico no Streamlit
    col2.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2, col3 = st.columns([4, 6, 1])

    col1.markdown('<p class="title">{}</p>'.format('% Completude'), unsafe_allow_html=True)
    col1.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)

    linha1 = ['Projetado', '1.50%', '2.00%', '3.00%', '10.00%', '15.00%', '17.00%', '20.00%', '30.00%', '31.00%', '33.00%']
    linha2 = ['Realizado', '1.50%', '2.00%', '3.00%', '10.00%', '15.00%', '17.00%', '20.00%', '30.00%', '31.00%', '33.00%']
    linha3 = ['Ajustado', '1.50%', '2.00%', '3.00%', '10.00%', '15.00%', '17.00%', '20.00%', '30.00%', '31.00%', '33.00%']
    linha4 = ['Simulado', '1.50%', '2.00%', '3.00%', '10.00%', '15.00%', '17.00%', '20.00%', '30.00%', '31.00%', '33.00%']

    array_fluxo_caixa = np.array([linha1, linha2, linha3, linha4])
    df_fluxo = pd.DataFrame(array_fluxo_caixa, columns=['Visão', 'Mês1', 'Mês2', 'Mês3', 'Mês4', 'Mês5', 'Mês6',
                                                        'Mês7', 'Mês8', 'Mês9', 'Mês10'])
    col1.dataframe(df_fluxo, hide_index=True)

    select_3 = col2.selectbox('Qual a visão desejada?', ('Projetado', 'Realizado', 'Ajustado', 'Simulado'))
    # Dados do gráfico de linha
    x_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_line = ['1.01', '2.23', '3.45', '4.80', '5.78', '6.84', '7.84', '8.58', '9.90', '10.58', '11.80', '13.58']

    # Dados do gráfico de barras (eixo secundário)
    x_bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_bar = [4000, 13000, 50000, 15000, 12000, 70000, 59000, 89000, 40000, 125500, 15000, 84000]

    # Criar o gráfico principal de linha
    fig = make_subplots(specs=[[{'secondary_y': True}]])

    fig.add_trace(go.Bar(x=x_bar, y=y_bar, name='Outra Métrica',opacity=0.5), secondary_y=True )
    fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines+markers', name='Série Temporal'))

    fig.update_traces(hovertemplate='%{y:.2f}%<br>%{x}')
    fig.update_layout(
        xaxis_title='Mês',
        title='Série Temporal com Eixo Secundário',
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            orientation="h",
        )
    )

    # Exibir o gráfico no Streamlit
    col2.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2, col3 = st.columns([4, 6, 1])

    col1.markdown('<p class="title">{}</p>'.format('Despesas'), unsafe_allow_html=True)
    col1.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)

    linha1 = ['Despesa1', 'R$ 100', 'R$ 200', 'R$ 300', 'R$250', 'R$150', 'R$ 500', 'R$400', 'R$750', 'R$1000',
              'R$1500']
    linha2 = ['Despesa2', 'R$ 100', 'R$ 200', 'R$ 300', 'R$250', 'R$150', 'R$ 500', 'R$400', 'R$750', 'R$1000',
              'R$1500']
    linha3 = ['Despesa3', 'R$ 100', 'R$ 200', 'R$ 300', 'R$250', 'R$150', 'R$ 500', 'R$400', 'R$750', 'R$1000',
              'R$1500']
    linha4 = ['Despesa4', 'R$ 100', 'R$ 200', 'R$ 300', 'R$250', 'R$150', 'R$ 500', 'R$400', 'R$750', 'R$1000',
              'R$1500']

    array_fluxo_caixa = np.array([linha1, linha2, linha3, linha4])
    df_fluxo = pd.DataFrame(array_fluxo_caixa, columns=['Visão', 'Mês1', 'Mês2', 'Mês3', 'Mês4', 'Mês5', 'Mês6',
                                                        'Mês7', 'Mês8', 'Mês9', 'Mês10'])
    col1.dataframe(df_fluxo, hide_index=True)

    select_4 = col2.selectbox('Qual a visão?', ('Projetado', 'Realizado', 'Ajustado', 'Simulado'))
    # Dados do gráfico de linha
    x_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_line = ['1.01', '2.23', '3.45', '4.80', '5.78', '6.84', '7.84', '8.58', '9.90', '10.58', '11.80', '13.58']

    # Dados do gráfico de barras (eixo secundário)
    x_bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_bar = [4000, 13000, 50000, 15000, 12000, 70000, 59000, 89000, 40000, 125500, 15000, 84000]

    # Criar o gráfico principal de linha
    fig = make_subplots(specs=[[{'secondary_y': True}]])

    fig.add_trace(go.Bar(x=x_bar, y=y_bar, name='Outra Métrica', opacity=0.5), secondary_y=True)
    fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines+markers', name='Série Temporal'))

    fig.update_traces(hovertemplate='%{y:.2f}%<br>%{x}')
    fig.update_layout(
        xaxis_title='Mês',
        title='Série Temporal com Eixo Secundário',
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            orientation="h",
        )
    )

    # Exibir o gráfico no Streamlit
    col2.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2, col3 = st.columns([4, 6, 1])

    col1.markdown('<p class="title">{}</p>'.format('Fluxo de Caixa'), unsafe_allow_html=True)
    col1.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)

    linha1 = ['Receita', '15000', '20000', '30000', '1000', '50000', '15000', '20000', '30000', '1000', '50000']
    linha2 = ['Despesa', '300', '500', '404', '100', '500', '300', '500', '400', '100', '500']
    linha3 = ['Saldo', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000']
    linha4 = ['Saldo Acumulado', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000',
              '10000']

    array_fluxo_caixa = np.array([linha1, linha2, linha3, linha4])
    df_fluxo = pd.DataFrame(array_fluxo_caixa, columns=['Dimensão', 'Mês1', 'Mês2', 'Mês3', 'Mês4', 'Mês5', 'Mês6',
                                                        'Mês7', 'Mês8', 'Mês9', 'Mês10'])
    col1.dataframe(df_fluxo, hide_index=True)

    select_4 = col2.selectbox('Qual sião espera ver?', ('Receita', 'Despesa', 'Saldo Acumulado'))
    fig = px.line(df_fluxo, x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                  y=[500, 400, 1200, 800, 1200, 2000, 1200, 900, 700, 1750, 500, 400], markers=True,
                  labels={'MÊS': 'RECEITA'}, width=1000)
    fig.update_traces(hovertemplate='%{y:.2f}%<br>%{x}')
    fig.update_layout(
        xaxis_title='MÊS',
        yaxis_title='RECEITA',
        title='Série Temporal'
    )
    col2.plotly_chart(fig, use_container_width=True)


if __name__ == '__main__':
        main()