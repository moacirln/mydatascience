import streamlit as st

def main():
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



    #Visual
    col1, col2 = st.columns([6,3])

    # Adicione o título dentro da caixa
    col1.markdown('<p class="boxed">{}</p>'.format('Cadastro Nova Obra'), unsafe_allow_html=True)

    col1,col2,col3 = st.columns([0.5,2,6])
    col1.markdown('<p class="fields">{}</p>'.format('ID:'), unsafe_allow_html=True)
    col2.markdown('<p class="fields">{}</p>'.format('52364785'), unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 4, 6])
    col1.markdown('<p class="fields">{}</p>'.format('Nome da Obra:'), unsafe_allow_html=True)
    nome_obra = col1.text_input("nome_obra", label_visibility = 'collapsed')
    col1.markdown('<p class="fields">{}</p>'.format('Empresa:'), unsafe_allow_html=True)
    nome_empresa = col1.text_input("nome_empresa", label_visibility='collapsed')

    st.divider()

    col1, col2 = st.columns([3, 6])
    col1.markdown('<p class="title">{}</p>'.format('Datas'), unsafe_allow_html=True)
    col1.markdown('<p class="fields">{}</p>'.format('Início das Vendas'), unsafe_allow_html=True)
    vendinha = col1.date_input("Inicio_Vendas", label_visibility='collapsed')
    col1.markdown('<p class="fields">{}</p>'.format('Início das Obras'), unsafe_allow_html=True)
    obrinha = col1.date_input("Inicio_Obras", label_visibility='collapsed')
    col1.markdown('<p class="fields">{}</p>'.format('Duração (Meses)'), unsafe_allow_html=True)
    Duracao = col1.number_input("Deuração", label_visibility='collapsed',)

    st.divider()

    col1,col3, col2 = st.columns([3,2,3])
    col1.markdown('<p class="title">{}</p>'.format('Escopo'), unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([3, 3, 3,2])
    col1.markdown('<p class="fields">{}</p>'.format('Qtd. MOD1'), unsafe_allow_html=True)
    Qtd_mod1 = col1.number_input("Qtd_mod1", label_visibility='collapsed')
    col3.markdown('<p class="fields">{}</p>'.format('Prç Médio MOD1'), unsafe_allow_html=True)
    Prç_mod1 = col3.number_input("Prç Médio Mod1", label_visibility='collapsed')

    col1.markdown('<p class="fields">{}</p>'.format('Qtd. MOD2'), unsafe_allow_html=True)
    Qtd_mod2 = col1.number_input("Qtd_mod2", label_visibility='collapsed')
    col3.markdown('<p class="fields">{}</p>'.format('Prç Médio MOD2'), unsafe_allow_html=True)
    Prç_mod2 = col3.number_input("Prç Médio Mod2", label_visibility='collapsed')

    col1.markdown('<p class="fields">{}</p>'.format('Qtd. MOD3'), unsafe_allow_html=True)
    Qtd_mod3 = col1.number_input("Qtd_mod3", label_visibility='collapsed')
    col3.markdown('<p class="fields">{}</p>'.format('Prç Médio MOD3'), unsafe_allow_html=True)
    Prç_mod3 = col3.number_input("Prç Médio Mod3", label_visibility='collapsed')

    st.divider()

    col1, col3, col2 = st.columns([3, 2, 3])
    col1.markdown('<p class="title">{}</p>'.format('Orçamento'), unsafe_allow_html=True)

    uploaded_orcamento = st.file_uploader("Escolha um arquivo de orçamento")

    st.divider()

    col1, col3, col2 = st.columns([3, 2, 3])
    col1.markdown('<p class="title">{}</p>'.format('% Completude'), unsafe_allow_html=True)

    uploaded_orcamento = st.file_uploader("Escolha um arquivo de % completude")


if __name__ == '__main__':
        main()
