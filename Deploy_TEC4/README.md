# ⚕️ Sistema de Predição de Obesidade

Sistema web desenvolvido com Streamlit para predição de níveis de obesidade utilizando Machine Learning (Random Forest).

## 📋 Descrição

Este sistema utiliza um modelo de Machine Learning treinado para classificar o nível de obesidade de pacientes com base em diversos fatores biométricos, hábitos alimentares e estilo de vida. É uma ferramenta de apoio ao diagnóstico médico que fornece predições com probabilidades detalhadas.

## 🎯 Categorias de Classificação

O sistema classifica os pacientes em 7 categorias:

- 🟢 **Abaixo do Peso** (Insufficient Weight)
- 🟢 **Peso Normal** (Normal Weight)
- 🟡 **Sobrepeso I** (Overweight Level I)
- 🟡 **Sobrepeso II** (Overweight Level II)
- 🔴 **Obesidade Tipo I** (Obesity Type I)
- 🔴 **Obesidade Tipo II** (Obesity Type II)
- 🔴 **Obesidade Tipo III** (Obesity Type III)

## 🔍 Variáveis Consideradas

### Dados Biométricos
- Gênero
- Idade (14-61 anos)
- Altura (1.45-1.98 m)
- Peso (39-173 kg)
- IMC (calculado automaticamente)

### Histórico e Hábitos Alimentares
- Histórico familiar de excesso de peso
- Consumo frequente de alimentos calóricos (FAVC)
- Frequência de consumo de vegetais (FCVC)
- Número de refeições principais por dia (NCP)
- Consumo de alimentos entre refeições (CAEC)

### Estilo de Vida
- Tabagismo (SMOKE)
- Consumo diário de água (CH2O)
- Monitoramento de ingestão calórica (SCC)
- Frequência de atividade física semanal (FAF)
- Tempo em dispositivos eletrônicos (TUE)
- Consumo de bebidas alcoólicas (CALC)
- Meio de transporte habitual (MTRANS)

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** - Interface web interativa
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Scikit-learn** - Machine Learning
- **Joblib** - Serialização de modelos
- **Plotly** - Visualizações interativas

## 📦 Estrutura do Projeto

```
obesity-prediction/
│
├── app_obesity_prediction.py          # Aplicativo principal Streamlit
├── random_forest_obesity_model.joblib # Modelo treinado
├── scaler_obesity.joblib              # Normalizador de features
├── label_encoder_obesity.joblib       # Codificador de labels
├── colunas_modelo.csv                 # Ordem das colunas do modelo
├── requirements.txt                   # Dependências Python
├── .gitignore                         # Arquivos ignorados pelo Git
└── README.md                          # Este arquivo
```

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/obesity-prediction.git
cd obesity-prediction
```

2. **Crie um ambiente virtual (recomendado)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o aplicativo**
```bash
streamlit run app_obesity_prediction.py
```

5. **Acesse no navegador**
O aplicativo será aberto automaticamente em `http://localhost:8501`

## 📊 Como Usar o Sistema

1. **Preencher Dados do Paciente**
   - Utilize a barra lateral esquerda para inserir todas as informações
   - Todos os campos são obrigatórios para uma predição precisa

2. **Realizar Predição**
   - Clique no botão "🔍 Realizar Predição"
   - Aguarde o processamento (geralmente instantâneo)

3. **Analisar Resultados**
   - Visualize a classificação predita com sua probabilidade
   - Analise o gráfico de distribuição de probabilidades
   - Revise a tabela detalhada com todas as probabilidades
   - Confira as informações do paciente resumidas

## 🔒 Aviso Importante

**⚠️ Este sistema é uma ferramenta de auxílio ao diagnóstico.** A avaliação e decisão final devem sempre ser realizadas por um profissional de saúde qualificado. Não substitui consultas médicas ou exames clínicos.

## 📈 Informações Técnicas do Modelo

- **Algoritmo:** Random Forest Classifier
- **Número de Estimadores:** 100 árvores
- **Total de Features:** 24 variáveis
- **Pré-processamento:**
  - Normalização com StandardScaler
  - Label Encoding para variáveis binárias
  - One-Hot Encoding para variáveis categóricas nominais

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido para auxiliar profissionais de saúde no diagnóstico e prevenção de obesidade.

## 📧 Contato

Para dúvidas, sugestões ou reportar problemas, abra uma [Issue](https://github.com/seu-usuario/obesity-prediction/issues) no GitHub.

---

**Desenvolvido com ❤️ usando Streamlit e Machine Learning**
