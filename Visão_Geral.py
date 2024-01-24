import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px

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
                           font-size: 36px;
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
    col1, col2 = st.columns([4, 5])

    # Adicione o título dentro da caixa
    col1.markdown('<p class="boxed">{}</p>'.format('Visão Geral'), unsafe_allow_html=True)
    selectvisao = st.selectbox('Qual visão deseja ver', ('Real', 'Projetado', 'Projetado Atualizado', 'Simulado'))


    col1, col2, col3 = st.columns([2,2,2])
    col1.markdown('<p class="fields">{}</p>'.format('Receita: R$ 2.000.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Despesa: R$ 700.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Fixo: R$ 200.000,00'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('Variável: R$ 500.000,00'), unsafe_allow_html=True)
    col3.markdown('<p class="fields">{}</p>'.format('Saldo: R$ 1.300.000,00'), unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns([3,6,1])

    # Criar dados por coluna
    coluna1 = ['Obra 1', 'Obra 2', 'Obra 3','Obra 4','Obra 5','Obra 6', 'Obra 7', 'Obra 8','Obra 9','Obra 10']
    coluna2 = ['2/30','8/30','15/30','1/30','31/30','2/30','8/30','15/30','1/30','31/30']
    coluna3 = ['15000', '20000','30000','1000','50000','15000', '20000','30000','1000','50000']
    coluna4 = ['30','50','40','10','50','30','50','40','10','50']
    coluna5= ['5%','10%','50%','1%','95%','5%','10%','50%','1%','95%']

    array_resultante = np.column_stack((coluna1, coluna2, coluna3, coluna4,coluna5))
    df = pd.DataFrame(array_resultante, columns=['OBRA', 'MÊS', 'RECEITA','VENDAS','% COMP.'])

    col1.markdown('<p class="title">{}</p>'.format('Obras'), unsafe_allow_html=True)
    col1.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)
    col1.dataframe(df, hide_index=True)
    col2.markdown('<div style="margin-top: 120px;"></div>', unsafe_allow_html=True)


    select = col2.selectbox('Qual dimensão deseja ver',('Receita', 'Vendas', '% Completude'))
    fig = px.line(df, x=[1,2,3,4,5,6,7,8,9,10,11,12], y=[1000,1200,800,400,1500,1000,1200,800,400,1500,2000,1000], markers=True,
                  labels={'MÊS': 'RECEITA'}, width=1000)
    fig.update_traces(hovertemplate='%{y:.2f}%<br>%{x}')
    fig.update_layout(
        xaxis_title='MÊS',
        yaxis_title='RECEITA',
        title='Série Temporal'
    )
    col2.plotly_chart(fig,use_container_width=True)

    st.divider()

    col1, col2, col3 = st.columns([4, 6, 1])

    col1.markdown('<p class="title">{}</p>'.format('Fluxo de Caixa'), unsafe_allow_html=True)
    col1.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)

    linha1 = ['Receita','15000', '20000', '30000', '1000', '50000', '15000', '20000', '30000', '1000', '50000']
    linha2 = ['Despesa','300', '500', '404', '100', '500', '300', '500', '400', '100', '500']
    linha3 = ['Saldo','10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000']
    linha4 = ['Saldo Acumulado','10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000', '10000']

    array_fluxo_caixa = np.array([linha1, linha2, linha3, linha4])
    df_fluxo = pd.DataFrame(array_fluxo_caixa, columns=['Dimensão', 'Mês1', 'Mês2', 'Mês3', 'Mês4', 'Mês5', 'Mês6',
                                                        'Mês7', 'Mês8','Mês9','Mês10'])
    col1.dataframe(df_fluxo, hide_index=True)

    select_2 = col2.selectbox('Qual dimensão deseja ver?', ('Receita', 'Despesa', 'Saldo Acumulado'))
    fig = px.line(df, x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
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
