import streamlit as st
import math

st.set_page_config(layout='wide')
e,centro,d=st.columns([1,5,1])
# PEGAR OS DADOS NECESSARIOS
with centro:
    st.header('Calculadora para obras pequenas')
    st.write('A calculadora ainda esta em desenvolvimento ha coisas a serem melhoradas')
    if 'resultado' not in st.session_state:
        st.session_state.resultado=None
    
    colunas=st.columns(2)
    with colunas[0]:
        ct=st.container(border=True)
        with ct:
            comprimento_parede = st.slider('Metros corridos da parede(m)', 0.01, 100.0,50.0, step=0.1)
            altura_parede = st.slider('Altura da parede(m)', 0.01, 10.0,5.0, step=0.1)
        ct=st.container(border=True)
        with ct:
            comprimento_bloco = st.slider('Comprimento do bloco(cm)', 0.01, 100.0,50.0, step=1.0) / 100
            altura_bloco = st.slider('Altura do bloco(cm)', 0.01, 100.0,50.0, step=1.0) / 100
        ct=st.container(border=True)
        with ct:
            reboco = st.slider('Espessura do reboco(cm)', 0.01, 10.0,5.0, step=0.1) / 100
        rendimento=st.number_input('Diga quantas partes de areia pra uma de cimento',0.001,10.0,5.0,step=1.0)
    with colunas[1]:
        cc=st.container(border=True)
        with cc:
            comprimento_chao = st.slider('Comprimento do chao(m)', 0.01, 10.0,5.0, step=0.1)
            largura_chao = st.slider('largura do chao(m)', 0.01, 10.0,5.0, step=0.5)
        cc=st.container(border=True)
        with cc:
            comprimento_porcelanato = st.slider('Comprimento do porcelanato(cm)', 0.1, 100.0,50.0, step=1.0) / 100
            largura_porcelanato = st.slider('Largura do porcelanato(cm)', 0.01, 100.0,50.0, step=1.0) / 100
        cc=st.container(border=True)
        with cc:
            contrapiso = st.slider('Espessura do contra piso(cm)', 0.01, 10.0,5.0, step=1.0) / 100
        demao=st.number_input('quantidade de demaos',0.001,3.0,2.0,step=1.0)
       
# with centro:
#     rendimento=st.number_input('Diga quantas partes de areia pra uma de cimento',0.001,10.0,3.0,step=1.0)
#     demao=st.number_input('quantidade de demaos',0.001,3.0,2.0,step=1.0)
#     st.divider()

# REALIZAR OS CALCULOS
    if st.button('CALCULAR',use_container_width=True):
        blocos=(comprimento_parede*altura_parede)/(comprimento_bloco*altura_bloco )
        vol_reboco=comprimento_parede*altura_parede*reboco*1/rendimento
        cimento_reboco=vol_reboco/0.03#(o 0.03 representa a quantidade de m3 que um saco de cimento geralmente rende)
        pisos=(largura_chao*comprimento_chao)/(largura_porcelanato*comprimento_porcelanato*1.10 )
        vol_contrapiso=largura_chao*comprimento_chao*contrapiso*1/rendimento
        cimento_contrapiso=vol_contrapiso/0.03
        tinta=comprimento_parede*altura_parede*demao/6

        st.session_state.resultado = {
            'blocos':blocos,
            'cimento_reboco': cimento_reboco,
            'pisos': pisos,
            'cimento_contrapiso': cimento_contrapiso,
            'tinta':tinta
        }

    # MOSTRAR OS RESULTADOS
    if st.session_state.resultado:
        contr=st.container(border=True)
        with contr:
            col = st.columns(5)
            result = st.session_state.resultado
            
            with col[0]:
                    st.metric("🧱 Blocos", f"{math.ceil(result['blocos']):.1f} ")
                    st.write('Unidades')
            with col[1]:
                    st.metric("🪣 Cimento reboco", f"{math.ceil(result['cimento_reboco']):.2f}")
                    st.write('Sacos')
            with col[2]:
                    st.metric("🧱 Pisos", f"{math.ceil(result['pisos']):.2f}")
                    st.write('Unidades')
            with col[3]:
                    st.metric("🪨 Cimento contrapiso", f"{math.ceil(result['cimento_contrapiso']):.2f}")
                    st.write('Sacos')
            with col[4]:
                    st.metric("🎨 Tinta", f"{math.ceil(result['tinta']):.2f}")
                    st.write('Litros')




#     st.title("📦 Materiais necessários")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.metric("🧱 Blocos", "3.509 un")

#     with col2:
#         st.metric("🪣 Cimento reboco", "55 sacos")

#     with col3:
#         st.metric("🎨 Tinta", "87 L")
# # cd projeto_streamlit
# streamlit run obra.py