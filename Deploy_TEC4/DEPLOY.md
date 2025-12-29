# 🚀 Guia Completo de Deploy no Streamlit Cloud

Este guia fornece instruções passo a passo para fazer o deploy do seu aplicativo de predição de obesidade no Streamlit Cloud através do GitHub.

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Preparação dos Arquivos](#preparação-dos-arquivos)
3. [Configuração do GitHub](#configuração-do-github)
4. [Deploy no Streamlit Cloud](#deploy-no-streamlit-cloud)
5. [Verificação e Teste](#verificação-e-teste)
6. [Troubleshooting](#troubleshooting)

---

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter:

- [ ] Conta no [GitHub](https://github.com) (criar se não tiver)
- [ ] Conta no [Streamlit Cloud](https://streamlit.io/cloud) (criar se não tiver)
- [ ] Git instalado no seu computador ([Download aqui](https://git-scm.com/downloads))
- [ ] Todos os arquivos do projeto:
  - `app_obesity_prediction.py`
  - `random_forest_obesity_model.joblib`
  - `scaler_obesity.joblib`
  - `label_encoder_obesity.joblib`
  - `colunas_modelo.csv`
  - `requirements.txt`
  - `.gitignore`
  - `README.md`

---

## 📁 Preparação dos Arquivos

### Passo 1: Organizar a Estrutura do Projeto

Crie uma pasta no seu computador com o nome do projeto (ex: `obesity-prediction`) e coloque todos os arquivos dentro dela:

```
obesity-prediction/
│
├── app_obesity_prediction.py
├── random_forest_obesity_model.joblib
├── scaler_obesity.joblib
├── label_encoder_obesity.joblib
├── colunas_modelo.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### Passo 2: Verificar o arquivo requirements.txt

Certifique-se de que o arquivo `requirements.txt` contém:

```
streamlit==1.31.1
pandas==2.2.0
numpy==1.26.3
joblib==1.3.2
plotly==5.18.0
scikit-learn==1.4.0
```

---

## 🐙 Configuração do GitHub

### Passo 3: Criar Repositório no GitHub

1. Acesse [GitHub](https://github.com)
2. Clique em **"New repository"** (ou ícone + no canto superior direito > "New repository")
3. Preencha os campos:
   - **Repository name:** `obesity-prediction` (ou outro nome de sua preferência)
   - **Description:** "Sistema de predição de obesidade usando Machine Learning"
   - **Visibilidade:** Escolha "Public" (recomendado para Streamlit Cloud gratuito)
   - **NÃO** marque "Add a README file" (já temos um)
4. Clique em **"Create repository"**

### Passo 4: Enviar Arquivos para o GitHub

Abra o terminal/prompt de comando na pasta do seu projeto e execute:

```bash
# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit: Obesity prediction app"

# Conectar ao repositório remoto (substitua SEU-USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU-USUARIO/obesity-prediction.git

# Renomear branch para main (se necessário)
git branch -M main

# Enviar para o GitHub
git push -u origin main
```

**Nota:** Se for a primeira vez usando Git, você precisará configurar seu nome e email:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

### Passo 5: Verificar Upload

1. Acesse seu repositório no GitHub: `https://github.com/SEU-USUARIO/obesity-prediction`
2. Verifique se todos os arquivos estão lá
3. Confirme que o `README.md` está sendo exibido na página principal

---

## ☁️ Deploy no Streamlit Cloud

### Passo 6: Acessar Streamlit Cloud

1. Acesse [Streamlit Cloud](https://streamlit.io/cloud)
2. Clique em **"Sign in"** (ou "Get started")
3. Escolha **"Continue with GitHub"**
4. Autorize o Streamlit a acessar sua conta do GitHub

### Passo 7: Criar Novo App

1. No dashboard do Streamlit Cloud, clique em **"New app"**
2. Preencha as informações:
   - **Repository:** Selecione `SEU-USUARIO/obesity-prediction`
   - **Branch:** `main`
   - **Main file path:** `app_obesity_prediction.py`
   - **App URL (opcional):** Personalize se desejar (ex: `obesity-predictor`)
3. Clique em **"Deploy!"**

### Passo 8: Aguardar Deploy

O Streamlit Cloud irá:
1. Clonar seu repositório
2. Instalar as dependências do `requirements.txt`
3. Executar o aplicativo

Isso pode levar de 2 a 5 minutos. Você verá logs em tempo real do processo.

---

## ✅ Verificação e Teste

### Passo 9: Testar o Aplicativo

Quando o deploy for concluído:

1. O aplicativo abrirá automaticamente em uma nova aba
2. A URL será algo como: `https://seu-app.streamlit.app`
3. Teste todas as funcionalidades:
   - [ ] Preencher dados na sidebar
   - [ ] Clicar em "Realizar Predição"
   - [ ] Verificar se os gráficos são exibidos
   - [ ] Testar com diferentes valores

### Passo 10: Compartilhar

Copie a URL do seu aplicativo e compartilhe!

---

## 🔧 Troubleshooting

### Problema: "Module not found"

**Solução:** Verifique se todas as bibliotecas estão no `requirements.txt` com as versões corretas.

### Problema: "File not found: random_forest_obesity_model.joblib"

**Solução:** 
1. Confirme que o arquivo está no repositório GitHub
2. Verifique se o nome do arquivo está exatamente igual no código e no repositório
3. Certifique-se de que o arquivo não foi bloqueado pelo `.gitignore`

### Problema: Deploy falha com erro de memória

**Solução:** O arquivo `random_forest_obesity_model.joblib` é grande (6.7MB). Se houver problemas:
1. Verifique se o arquivo foi enviado corretamente ao GitHub
2. Considere usar Git LFS (Large File Storage) para arquivos grandes:

```bash
git lfs install
git lfs track "*.joblib"
git add .gitattributes
git add *.joblib
git commit -m "Add model files with Git LFS"
git push
```

### Problema: App muito lento

**Solução:** 
1. O uso de `@st.cache_resource` no código já otimiza o carregamento do modelo
2. Certifique-se de que está usando a versão gratuita do Streamlit Cloud (recursos limitados)

### Problema: Não consigo fazer push para o GitHub

**Solução:**
1. Verifique suas credenciais do GitHub
2. Se usar autenticação de dois fatores, crie um Personal Access Token:
   - GitHub > Settings > Developer settings > Personal access tokens
   - Use o token como senha ao fazer push

---

## 🔄 Atualizando o Aplicativo

Para fazer alterações no aplicativo já deployado:

```bash
# Faça as alterações nos arquivos
# Adicione as mudanças
git add .

# Commit
git commit -m "Descrição das mudanças"

# Envie para o GitHub
git push
```

O Streamlit Cloud detectará automaticamente as mudanças e fará o redeploy!

---

## 📊 Monitoramento

### Acessar Logs

1. No Streamlit Cloud dashboard
2. Clique nos três pontinhos do seu app
3. Selecione "Logs"
4. Veja logs em tempo real de erros e acessos

### Gerenciar o App

No dashboard você pode:
- ⏸️ Pausar o app (economizar recursos)
- 🔄 Fazer reboot
- 🗑️ Deletar o app
- ⚙️ Configurar settings

---

## 🎉 Pronto!

Seu aplicativo está online e acessível para qualquer pessoa no mundo! 

**URL do seu app:** `https://SEU-APP.streamlit.app`

---

## 📞 Suporte

- **Documentação Streamlit:** https://docs.streamlit.io
- **Comunidade Streamlit:** https://discuss.streamlit.io
- **Issues GitHub:** Abra uma issue no seu repositório

---

## ✨ Dicas Extras

### Personalizar Domínio

No Streamlit Cloud (plano pago), você pode:
- Usar domínio personalizado
- Remover marca d'água do Streamlit
- Ter mais recursos computacionais

### Segurança

Para dados sensíveis, use `st.secrets`:
1. Crie arquivo `.streamlit/secrets.toml` localmente (não commite!)
2. No Streamlit Cloud: App settings > Secrets
3. Adicione suas variáveis secretas

### Analytics

Adicione Google Analytics ou outras ferramentas de tracking para monitorar uso do app.

---

**Boa sorte com seu deploy! 🚀**
