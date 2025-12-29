import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
try:
    import plotly.graph_objects as go
    import plotly.express as px
except Exception as e:
    st.error("A biblioteca 'plotly' não está instalada ou ocorreu um erro ao importá-la. Instale com: `pip install plotly` ou rode `pip install -r Deploy_TEC4/requirements.txt`.")
    st.stop()

# Configuração da página
st.set_page_config(
    page_title="Predição de Obesidade",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar a aparência
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-header">⚕️ Sistema de Predição de Obesidade</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Modelo de Machine Learning para auxílio ao diagnóstico médico</p>', unsafe_allow_html=True)

# Carregar o modelo e os componentes
@st.cache_resource
def load_model_components():
    try:
        base_dir = Path(__file__).resolve().parent
        model_path = base_dir / 'random_forest_obesity_model.joblib'
        scaler_path = base_dir / 'scaler_obesity.joblib'
        label_encoder_path = base_dir / 'label_encoder_obesity.joblib'
        columns_path = base_dir / 'colunas_modelo.csv'

        # Verificar arquivos necessários
        missing = [p.name for p in (model_path, scaler_path, label_encoder_path, columns_path) if not p.exists()]
        if missing:
            raise FileNotFoundError(f"Arquivos ausentes: {', '.join(missing)} no diretório {str(base_dir)}. Verifique se os arquivos foram copiados para a pasta do app.")

        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        label_encoder = joblib.load(label_encoder_path)
        
        # Carregar as colunas do modelo
        colunas_df = pd.read_csv(columns_path)
        # Garantir que pegamos a primeira coluna como lista de nomes (compatível com CSVs simples)
        model_columns = colunas_df.iloc[:, 0].astype(str).tolist()
        
        return model, scaler, label_encoder, model_columns
    except Exception as e:
        st.error(f"Erro ao carregar os componentes do modelo: {str(e)}")
        return None, None, None, None

model, scaler, label_encoder, model_columns = load_model_components()

if model is None:
    st.error("⚠️ Não foi possível carregar o modelo. Verifique se os arquivos estão no diretório correto.")
    st.stop()

# Função para preparar os dados de entrada
def prepare_input_data(user_inputs):
    # Criar DataFrame com as colunas básicas
    input_df = pd.DataFrame([{
        'Gender': user_inputs['gender_encoded'],
        'Age': user_inputs['age'],
        'Height': user_inputs['height'],
        'Weight': user_inputs['weight'],
        'family_history': user_inputs['family_history_encoded'],
        'FAVC': user_inputs['favc_encoded'],
        'FCVC': user_inputs['fcvc'],
        'NCP': user_inputs['ncp'],
        'SMOKE': user_inputs['smoke_encoded'],
        'CH2O': user_inputs['ch2o'],
        'SCC': user_inputs['scc_encoded'],
        'FAF': user_inputs['faf'],
        'TUE': user_inputs['tue'],
    }])
    
    # Adicionar colunas dummy para CAEC
    caec_cols = ['CAEC_Frequently', 'CAEC_Sometimes', 'CAEC_no']
    for col in caec_cols:
        input_df[col] = 0
    if user_inputs['caec'] == 'Frequently':
        input_df['CAEC_Frequently'] = 1
    elif user_inputs['caec'] == 'Sometimes':
        input_df['CAEC_Sometimes'] = 1
    elif user_inputs['caec'] == 'no':
        input_df['CAEC_no'] = 1
    
    # Adicionar colunas dummy para CALC
    calc_cols = ['CALC_Frequently', 'CALC_Sometimes', 'CALC_no']
    for col in calc_cols:
        input_df[col] = 0
    if user_inputs['calc'] == 'Frequently':
        input_df['CALC_Frequently'] = 1
    elif user_inputs['calc'] == 'Sometimes':
        input_df['CALC_Sometimes'] = 1
    elif user_inputs['calc'] == 'no':
        input_df['CALC_no'] = 1
    
    # Adicionar colunas dummy para MTRANS
    mtrans_cols = ['MTRANS_Bike', 'MTRANS_Motorbike', 'MTRANS_Public_Transportation', 'MTRANS_Walking']
    for col in mtrans_cols:
        input_df[col] = 0
    if user_inputs['mtrans'] == 'Bike':
        input_df['MTRANS_Bike'] = 1
    elif user_inputs['mtrans'] == 'Motorbike':
        input_df['MTRANS_Motorbike'] = 1
    elif user_inputs['mtrans'] == 'Public_Transportation':
        input_df['MTRANS_Public_Transportation'] = 1
    elif user_inputs['mtrans'] == 'Walking':
        input_df['MTRANS_Walking'] = 1
    
    # Garantir que as colunas estejam na ordem correta
    input_df = input_df[model_columns]
    
    return input_df

# Sidebar para inputs
st.sidebar.header("📋 Dados do Paciente")

with st.sidebar:
    st.subheader("Informações Pessoais")
    
    gender = st.selectbox("Gênero", ["Female", "Male"], help="Sexo biológico do paciente")
    gender_encoded = 0 if gender == "Female" else 1
    
    age = st.slider("Idade (anos)", 14, 61, 25, help="Idade do paciente em anos")
    
    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input("Altura (m)", 1.45, 1.98, 1.70, 0.01, help="Altura em metros")
    with col2:
        weight = st.number_input("Peso (kg)", 39, 173, 70, 1, help="Peso em quilogramas")
    
    # Calcular IMC
    bmi = weight / (height ** 2)
    st.metric("IMC Calculado", f"{bmi:.2f}")
    
    st.divider()
    st.subheader("Histórico e Hábitos Alimentares")
    
    family_history = st.radio("Histórico familiar de excesso de peso", ["Não", "Sim"])
    family_history_encoded = 0 if family_history == "Não" else 1
    
    favc = st.radio("Consumo frequente de alimentos calóricos", ["Não", "Sim"])
    favc_encoded = 0 if favc == "Não" else 1
    
    fcvc = st.select_slider(
        "Frequência de consumo de vegetais",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Raramente", 2: "Às vezes", 3: "Sempre"}[x],
        help="1=Raramente, 2=Às vezes, 3=Sempre"
    )
    
    ncp = st.select_slider(
        "Número de refeições principais por dia",
        options=[1, 2, 3, 4],
        value=3,
        help="Quantidade de refeições principais diárias"
    )
    
    caec = st.selectbox(
        "Consumo de alimentos entre refeições",
        ["no", "Sometimes", "Frequently", "Always"],
        format_func=lambda x: {"no": "Não", "Sometimes": "Às vezes", "Frequently": "Frequentemente", "Always": "Sempre"}[x]
    )
    
    st.divider()
    st.subheader("Estilo de Vida")
    
    smoke = st.radio("Fumante", ["Não", "Sim"])
    smoke_encoded = 0 if smoke == "Não" else 1
    
    ch2o = st.select_slider(
        "Consumo diário de água",
        options=[1, 2, 3],
        value=2,
        format_func=lambda x: {1: "< 1L/dia", 2: "1-2L/dia", 3: "> 2L/dia"}[x]
    )
    
    scc = st.radio("Monitora a ingestão calórica", ["Não", "Sim"])
    scc_encoded = 0 if scc == "Não" else 1
    
    faf = st.select_slider(
        "Frequência de atividade física (por semana)",
        options=[0, 1, 2, 3],
        value=1,
        format_func=lambda x: {0: "Nenhuma", 1: "1-2x", 2: "3-4x", 3: "5x ou mais"}[x]
    )
    
    tue = st.select_slider(
        "Tempo diário em dispositivos eletrônicos",
        options=[0, 1, 2],
        value=1,
        format_func=lambda x: {0: "0-2h/dia", 1: "3-5h/dia", 2: "> 5h/dia"}[x]
    )
    
    calc = st.selectbox(
        "Consumo de bebidas alcoólicas",
        ["no", "Sometimes", "Frequently", "Always"],
        format_func=lambda x: {"no": "Não", "Sometimes": "Às vezes", "Frequently": "Frequentemente", "Always": "Sempre"}[x]
    )
    
    mtrans = st.selectbox(
        "Meio de transporte habitual",
        ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"],
        format_func=lambda x: {
            "Automobile": "Automóvel",
            "Motorbike": "Moto",
            "Bike": "Bicicleta",
            "Public_Transportation": "Transporte Público",
            "Walking": "A pé"
        }[x]
    )

# Preparar inputs
user_inputs = {
    'gender_encoded': gender_encoded,
    'age': age,
    'height': height,
    'weight': weight,
    'family_history_encoded': family_history_encoded,
    'favc_encoded': favc_encoded,
    'fcvc': fcvc,
    'ncp': ncp,
    'smoke_encoded': smoke_encoded,
    'ch2o': ch2o,
    'scc_encoded': scc_encoded,
    'faf': faf,
    'tue': tue,
    'caec': caec,
    'calc': calc,
    'mtrans': mtrans
}

# Botão de predição
if st.sidebar.button("🔍 Realizar Predição", type="primary", use_container_width=True):
    try:
        # Preparar dados
        input_data = prepare_input_data(user_inputs)
        
        # Fazer predição
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        
        # Decodificar a predição
        class_names = label_encoder.classes_
        predicted_class = label_encoder.inverse_transform([prediction])[0]
        
        # Traduzir nomes das classes
        class_translation = {
            'Insufficient_Weight': 'Abaixo do Peso',
            'Normal_Weight': 'Peso Normal',
            'Overweight_Level_I': 'Sobrepeso I',
            'Overweight_Level_II': 'Sobrepeso II',
            'Obesity_Type_I': 'Obesidade Tipo I',
            'Obesity_Type_II': 'Obesidade Tipo II',
            'Obesity_Type_III': 'Obesidade Tipo III'
        }
        
        # Exibir resultado principal
        st.header("📊 Resultado da Predição")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Determinar cor baseada na classificação
            if 'Obesity' in predicted_class:
                alert_type = "error"
                emoji = "🔴"
            elif 'Overweight' in predicted_class:
                alert_type = "warning"
                emoji = "🟡"
            else:
                alert_type = "success"
                emoji = "🟢"
            
            st.info(f"### {emoji} Classificação Predita: **{class_translation[predicted_class]}**")
            
            # Probabilidade da classe predita
            max_prob = probabilities[prediction] * 100
            st.metric("Probabilidade", f"{max_prob:.2f}%")
        
        st.divider()
        
        # Criar visualizações
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Distribuição de Probabilidades")
            
            # Preparar dados para o gráfico
            prob_df = pd.DataFrame({
                'Categoria': [class_translation[c] for c in class_names],
                'Probabilidade': probabilities * 100
            }).sort_values('Probabilidade', ascending=True)
            
            # Gráfico de barras horizontais
            fig_bar = px.bar(
                prob_df,
                x='Probabilidade',
                y='Categoria',
                orientation='h',
                text=prob_df['Probabilidade'].apply(lambda x: f'{x:.1f}%'),
                color='Probabilidade',
                color_continuous_scale='RdYlGn_r',
                labels={'Probabilidade': 'Probabilidade (%)'}
            )
            
            fig_bar.update_traces(textposition='outside')
            fig_bar.update_layout(
                showlegend=False,
                height=400,
                xaxis_title="Probabilidade (%)",
                yaxis_title="",
                coloraxis_showscale=False
            )
            
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            st.subheader("🥧 Distribuição em Pizza")
            
            # Gráfico de pizza
            fig_pie = go.Figure(data=[go.Pie(
                labels=[class_translation[c] for c in class_names],
                values=probabilities,
                hole=0.4,
                textinfo='label+percent',
                marker=dict(colors=px.colors.sequential.RdBu_r)
            )])
            
            fig_pie.update_layout(
                height=400,
                showlegend=True,
                legend=dict(
                    orientation="v",
                    yanchor="middle",
                    y=0.5,
                    xanchor="left",
                    x=1.02
                )
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
        
        st.divider()
        
        # Tabela detalhada de probabilidades
        st.subheader("📋 Probabilidades Detalhadas")
        
        prob_table = pd.DataFrame({
            'Categoria': [class_translation[c] for c in class_names],
            'Probabilidade': [f"{p*100:.2f}%" for p in probabilities],
            'Valor Numérico': probabilities
        }).sort_values('Valor Numérico', ascending=False)
        
        prob_table = prob_table.drop('Valor Numérico', axis=1)
        prob_table.index = range(1, len(prob_table) + 1)
        
        st.dataframe(prob_table, use_container_width=True)
        
        # Informações adicionais
        st.divider()
        st.subheader("ℹ️ Informações do Paciente")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Idade", f"{age} anos")
            st.metric("Gênero", gender)
        
        with col2:
            st.metric("Altura", f"{height} m")
            st.metric("Peso", f"{weight} kg")
        
        with col3:
            st.metric("IMC", f"{bmi:.2f}")
            st.metric("Atividade Física", {0: "Nenhuma", 1: "1-2x/sem", 2: "3-4x/sem", 3: "5x+/sem"}[faf])
        
        with col4:
            st.metric("Histórico Familiar", family_history)
            st.metric("Consumo de Água", {1: "< 1L", 2: "1-2L", 3: "> 2L"}[ch2o])
        
        # Aviso médico
        st.warning("⚠️ **Aviso Importante:** Este sistema é uma ferramenta de auxílio ao diagnóstico. A avaliação e decisão final devem sempre ser realizadas por um profissional de saúde qualificado.")
        
    except Exception as e:
        st.error(f"Erro ao realizar a predição: {str(e)}")
        st.exception(e)
else:
    # Tela inicial quando não há predição
    st.info("👈 **Preencha os dados do paciente na barra lateral e clique em 'Realizar Predição' para obter os resultados.**")
    
    # Informações sobre o modelo
    with st.expander("ℹ️ Sobre o Sistema"):
        st.markdown("""
        ### Sistema de Predição de Obesidade
        
        Este sistema utiliza um modelo de **Machine Learning (Random Forest)** treinado para classificar o nível de obesidade 
        de um paciente com base em diversos fatores:
        
        #### Categorias de Classificação:
        - 🟢 **Abaixo do Peso** (Insufficient Weight)
        - 🟢 **Peso Normal** (Normal Weight)
        - 🟡 **Sobrepeso I** (Overweight Level I)
        - 🟡 **Sobrepeso II** (Overweight Level II)
        - 🔴 **Obesidade Tipo I** (Obesity Type I)
        - 🔴 **Obesidade Tipo II** (Obesity Type II)
        - 🔴 **Obesidade Tipo III** (Obesity Type III)
        
        #### Variáveis Consideradas:
        - Dados biométricos (idade, altura, peso, gênero)
        - Histórico familiar
        - Hábitos alimentares
        - Nível de atividade física
        - Estilo de vida (consumo de água, tempo em eletrônicos, etc.)
        - Meio de transporte utilizado
        
        #### Como Usar:
        1. Preencha todos os campos na barra lateral esquerda
        2. Clique no botão "Realizar Predição"
        3. Analise os resultados e probabilidades apresentados
        
        **Importante:** Este é um sistema de apoio à decisão médica e não substitui a avaliação profissional.
        """)
    
    with st.expander("📊 Estatísticas do Modelo"):
        st.markdown("""
        ### Informações Técnicas
        
        - **Algoritmo:** Random Forest Classifier
        - **Número de Estimadores:** 100 árvores
        - **Features utilizadas:** 24 variáveis
        - **Pré-processamento:** 
          - Normalização com StandardScaler
          - Label Encoding para variáveis categóricas
          - One-Hot Encoding para variáveis nominais
        
        O modelo foi treinado com dados de pacientes e utiliza técnicas de ensemble learning 
        para garantir predições mais robustas e confiáveis.
        """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Sistema de Predição de Obesidade | Machine Learning para Saúde</p>
    <p style='font-size: 0.8rem;'>Desenvolvido para auxiliar profissionais de saúde no diagnóstico e prevenção</p>
</div>
""", unsafe_allow_html=True)
