# 📊 Dashboard Interativo de Análise de Obesidade

## Descrição

Dashboard profissional desenvolvido para análise médica de dados de obesidade, permitindo à equipe médica explorar correlações entre variáveis demográficas, comportamentais e os níveis de obesidade dos pacientes.

## 🎯 Funcionalidades Principais

### 1. **Filtros Interativos**
- Filtro por sexo (Masculino/Feminino)
- Filtro por faixa etária (18-25, 26-35, 36-45, 46+)
- Filtro por nível de obesidade
- Filtro por histórico familiar de sobrepeso

### 2. **Cards de Estatísticas em Tempo Real**
- Total de pacientes filtrados
- IMC médio
- Idade média
- Percentual de obesidade

### 3. **Abas de Análise**

#### 📊 Aba Distribuições
- Distribuição por nível de obesidade
- Distribuição de IMC por sexo (boxplot)
- Distribuição de idade (histograma)
- Relação peso x altura por obesidade (scatter plot)

#### 🔄 Aba Correlações
- Matriz de correlação entre variáveis numéricas
- IMC vs frequência de atividade física
- IMC médio por variáveis categóricas
- Consumo de água vs IMC

#### 📈 Aba Comparações
- Consumo de vegetais por nível de obesidade
- Atividade física por obesidade
- Meio de transporte vs obesidade
- Tempo de uso de tecnologia vs IMC

#### 📋 Aba Tabela de Dados
- Tabela interativa com todos os dados
- Ordenação por qualquer coluna
- Filtros dinâmicos
- Exportação para Excel
- Estatísticas resumidas

## 🔧 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Instalar Dependências

```bash
pip install pandas numpy plotly dash dash-bootstrap-components
```

### Passo 2: Preparar Dados

Certifique-se de que o arquivo `Obesity_Tratado.csv` está na mesma pasta do script Python.

### Passo 3: Executar o Dashboard

```bash
python dashboard_obesidade_interativo.py
```

## 🚀 Como Usar

1. **Inicie o aplicativo** executando o comando acima
2. **Acesse no navegador** em: `http://127.0.0.1:8050/`
3. **Use os filtros** no painel esquerdo para segmentar os dados
4. **Navegue pelas abas** para diferentes análises
5. **Interaja com os gráficos**:
   - Passe o mouse sobre os pontos para ver detalhes
   - Clique e arraste para dar zoom
   - Clique duplo para resetar zoom
   - Use a legenda para ocultar/mostrar categorias

## 📊 Variáveis Disponíveis

### Variáveis Demográficas
- **Sexo**: Masculino/Feminino
- **Idade**: Idade do paciente
- **Altura**: Altura em metros
- **Peso**: Peso em quilogramas
- **IMC**: Índice de Massa Corporal (calculado automaticamente)

### Variáveis Comportamentais
- **Histórico Familiar**: Histórico familiar de sobrepeso
- **FAVC**: Consumo frequente de alimentos calóricos
- **FCVC**: Frequência de consumo de vegetais
- **NCP**: Número de refeições principais
- **CAEC**: Consumo de alimentos entre refeições
- **SMOKE**: Fumante
- **CH2O**: Consumo diário de água
- **SCC**: Monitora consumo de calorias
- **FAF**: Frequência de atividade física
- **TUE**: Tempo de uso de tecnologia
- **CALC**: Consumo de álcool
- **MTRANS**: Meio de transporte

### Variável Alvo
- **Obesity**: Nível de obesidade
  - Peso Insuficiente
  - Peso Normal
  - Sobrepeso Nível I
  - Sobrepeso Nível II
  - Obesidade Tipo I
  - Obesidade Tipo II
  - Obesidade Tipo III

## 💡 Insights que o Dashboard Permite Identificar

1. **Perfil Demográfico**: Distribuição de obesidade por idade e sexo
2. **Correlações Comportamentais**: Relação entre hábitos alimentares e obesidade
3. **Impacto da Atividade Física**: Como exercícios influenciam o IMC
4. **Fatores de Risco**: Identificação de variáveis associadas a maior obesidade
5. **Padrões de Estilo de Vida**: Relação entre transporte, tecnologia e obesidade
6. **Hereditariedade**: Impacto do histórico familiar

## 🎨 Personalização

O dashboard pode ser facilmente personalizado:

1. **Cores**: Altere a variável `CORES` no código
2. **Gráficos**: Adicione novos gráficos nas funções `criar_aba_*`
3. **Filtros**: Adicione novos filtros na seção de layout
4. **Métricas**: Adicione novos cards de estatísticas

## 📝 Estrutura do Código

```
dashboard_obesidade_interativo.py
├── Importações e configurações
├── Carregamento e preparação dos dados
├── Configuração do aplicativo Dash
├── Layout do dashboard
│   ├── Cabeçalho
│   ├── Painel de filtros
│   ├── Cards de estatísticas
│   └── Abas de visualização
├── Callbacks (interatividade)
│   ├── Atualizar cards
│   └── Renderizar conteúdo das abas
├── Funções de criação de abas
│   ├── criar_aba_distribuicao()
│   ├── criar_aba_correlacoes()
│   ├── criar_aba_comparacoes()
│   └── criar_aba_tabela()
└── Execução do aplicativo
```

## 🔒 Requisitos de Sistema

- **Memória RAM**: Mínimo 4GB recomendado
- **Navegador**: Chrome, Firefox, Safari ou Edge (versões atualizadas)
- **Resolução**: Mínimo 1366x768 para melhor visualização

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências foram instaladas
2. Confirme que o arquivo CSV está no diretório correto
3. Verifique se a porta 8050 está disponível

## 📄 Licença

Dashboard desenvolvido para uso interno da equipe médica.

---

**Desenvolvido para análise profissional de dados de obesidade**
Versão 1.0 - 2026
