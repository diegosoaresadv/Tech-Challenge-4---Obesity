# 🚀 Guia Rápido de Deploy - 5 Minutos

## ⚡ Passos Essenciais

### 1️⃣ Preparar Arquivos (2 min)
```bash
# Coloque todos os arquivos em uma pasta:
# - app_obesity_prediction.py
# - random_forest_obesity_model.joblib
# - scaler_obesity.joblib
# - label_encoder_obesity.joblib
# - colunas_modelo.csv
# - requirements.txt
# - .gitignore
# - README.md
```

### 2️⃣ Criar Repositório no GitHub (1 min)
1. Vá em https://github.com/new
2. Nome: `obesity-prediction`
3. Public
4. Create repository

### 3️⃣ Upload via Terminal (1 min)
```bash
cd sua-pasta-do-projeto
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/SEU-USUARIO/obesity-prediction.git
git branch -M main
git push -u origin main
```

### 4️⃣ Deploy no Streamlit Cloud (1 min)
1. Acesse https://streamlit.io/cloud
2. Login with GitHub
3. New app
4. Selecione seu repositório
5. Main file: `app_obesity_prediction.py`
6. Deploy!

### ✅ Pronto!
Aguarde 2-5 minutos e seu app estará online!

---

## 🆘 Problemas Comuns

**Erro ao fazer push:**
```bash
# Configure Git primeiro
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

**Module not found:**
- Verifique `requirements.txt`

**File not found:**
- Confirme que todos os arquivos `.joblib` e `.csv` foram enviados ao GitHub

---

## 📱 Próximos Passos

Depois do deploy:
- Teste o app
- Compartilhe a URL
- Configure analytics (opcional)
- Personalize domínio (plano pago)

**Documentação completa:** Veja `DEPLOY.md`
