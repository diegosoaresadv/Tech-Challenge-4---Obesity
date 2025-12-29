# 🚀 DEPLOY EM 3 PASSOS

## Você tem tudo que precisa!

Este pacote contém **14 arquivos** prontos para deploy no Streamlit Cloud.

---

## ⚡ DEPLOY RÁPIDO (10 minutos)

### 1️⃣ GITHUB (3 min)
```bash
# Abra o terminal na pasta dos arquivos e execute:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git branch -M main
git push -u origin main
```

### 2️⃣ STREAMLIT CLOUD (2 min)
1. Vá em https://streamlit.io/cloud
2. Login com GitHub
3. New app → selecione seu repositório
4. Main file: `app_obesity_prediction.py`
5. Deploy!

### 3️⃣ AGUARDE (5 min)
- Deploy automático
- App online!
- URL: `https://seu-app.streamlit.app`

---

## 📚 DOCUMENTAÇÃO COMPLETA

### Primeira vez com Git/GitHub/Streamlit?
👉 Leia: **DEPLOY.md** (guia completo passo a passo)

### Com pressa?
👉 Leia: **QUICK_START.md** (versão resumida)

### Quer garantir que não esqueceu nada?
👉 Use: **CHECKLIST.md** (marque cada etapa)

### Problemas com comandos Git?
👉 Consulte: **GIT_COMMANDS.md** (referência rápida)

### Quer entender o projeto?
👉 Veja: **README.md** (documentação do app)

### Não sabe por onde começar?
👉 Comece com: **00_LEIA_PRIMEIRO.md** (índice geral)

---

## ✅ ARQUIVOS INCLUÍDOS

### Essenciais (sem estes o app não funciona):
- ✅ app_obesity_prediction.py
- ✅ random_forest_obesity_model.joblib
- ✅ scaler_obesity.joblib  
- ✅ label_encoder_obesity.joblib
- ✅ colunas_modelo.csv
- ✅ requirements.txt

### Recomendados:
- ✅ README.md
- ✅ .gitignore
- ✅ LICENSE

### Documentação:
- ✅ DEPLOY.md
- ✅ QUICK_START.md
- ✅ CHECKLIST.md
- ✅ GIT_COMMANDS.md
- ✅ 00_LEIA_PRIMEIRO.md

### Configuração (opcional):
- ✅ .streamlit/config.toml

---

## 🎯 QUAL ARQUIVO LER?

| Situação | Arquivo |
|----------|---------|
| Primeira vez fazendo deploy | DEPLOY.md |
| Já fiz deploy antes, só preciso relembrar | QUICK_START.md |
| Quero uma checklist | CHECKLIST.md |
| Problemas com Git | GIT_COMMANDS.md |
| Entender o projeto | README.md |
| Visão geral de tudo | 00_LEIA_PRIMEIRO.md |

---

## 🆘 PROBLEMAS COMUNS

### "Authentication failed" no Git
→ Configure: `git config --global user.name "Nome"`
→ Configure: `git config --global user.email "email@exemplo.com"`

### "File not found" no Streamlit
→ Verifique se todos os arquivos .joblib e .csv estão no GitHub

### "Module not found" 
→ Verifique se o requirements.txt está no repositório

### Outros problemas
→ Veja seção Troubleshooting no DEPLOY.md

---

## 💡 DICA IMPORTANTE

**TESTE LOCALMENTE PRIMEIRO!**

Antes de fazer deploy, teste se funciona:

```bash
# Instale as dependências
pip install -r requirements.txt

# Execute o app
streamlit run app_obesity_prediction.py
```

Se funcionar localmente, funcionará no Streamlit Cloud!

---

## 📞 PRECISA DE AJUDA?

1. Consulte primeiro a documentação incluída
2. Veja o Troubleshooting no DEPLOY.md
3. Docs oficiais: https://docs.streamlit.io

---

## ✨ ESTÁ PRONTO!

Você tem todos os arquivos necessários. Basta seguir os 3 passos acima ou ler a documentação detalhada.

**Boa sorte! 🚀**

---

**Versão:** 1.0 | **Data:** Dezembro 2024
