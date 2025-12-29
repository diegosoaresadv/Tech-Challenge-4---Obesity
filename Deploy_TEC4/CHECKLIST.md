# ✅ Checklist de Deploy - Obesidade Prediction App

Use este checklist para garantir que nada seja esquecido no processo de deploy.

## 📦 Antes de Começar

- [ ] Tenho uma conta no GitHub (criar em https://github.com/signup)
- [ ] Tenho uma conta no Streamlit Cloud (criar em https://streamlit.io/cloud)
- [ ] Tenho Git instalado no computador (verificar com `git --version`)
- [ ] Tenho todos os arquivos do projeto baixados

## 📁 Arquivos Necessários (8 arquivos)

- [ ] `app_obesity_prediction.py` (16 KB)
- [ ] `random_forest_obesity_model.joblib` (6.7 MB)
- [ ] `scaler_obesity.joblib` (1 KB)
- [ ] `label_encoder_obesity.joblib` (1 KB)
- [ ] `colunas_modelo.csv` (512 bytes)
- [ ] `requirements.txt`
- [ ] `.gitignore`
- [ ] `README.md`

**Opcional mas recomendado:**
- [ ] `DEPLOY.md` (guia completo)
- [ ] `QUICK_START.md` (guia rápido)
- [ ] `.streamlit/config.toml` (configurações)

## 🐙 Configuração do GitHub

- [ ] Repositório criado no GitHub
- [ ] Nome do repositório anotado: _______________
- [ ] Repositório configurado como Public
- [ ] Git configurado no terminal (nome e email)

## 📤 Upload para GitHub

- [ ] Navegado até a pasta do projeto no terminal
- [ ] Executado `git init`
- [ ] Executado `git add .`
- [ ] Executado `git commit -m "Initial commit"`
- [ ] Executado `git remote add origin [URL]`
- [ ] Executado `git branch -M main`
- [ ] Executado `git push -u origin main`
- [ ] Verificado que todos os arquivos aparecem no GitHub

## ☁️ Deploy no Streamlit Cloud

- [ ] Acessado https://streamlit.io/cloud
- [ ] Login feito com GitHub
- [ ] Clicado em "New app"
- [ ] Repositório selecionado
- [ ] Branch: `main`
- [ ] Main file: `app_obesity_prediction.py`
- [ ] URL personalizada escolhida (opcional): _______________
- [ ] Clicado em "Deploy"
- [ ] Aguardado conclusão do deploy (2-5 min)

## 🧪 Testes

- [ ] App abriu sem erros
- [ ] Sidebar carrega todos os campos
- [ ] Consegue preencher todos os dados
- [ ] Botão "Realizar Predição" funciona
- [ ] Gráficos são exibidos corretamente
- [ ] Gráfico de barras aparece
- [ ] Gráfico de pizza aparece
- [ ] Tabela de probabilidades aparece
- [ ] Informações do paciente são exibidas
- [ ] Testado com diferentes valores

## 🎉 Finalização

- [ ] URL do app anotada: _______________
- [ ] App compartilhado com colegas/clientes
- [ ] README.md revisado no GitHub
- [ ] Screenshots tiradas (opcional)

## 📊 Monitoramento (Opcional)

- [ ] Configurado analytics
- [ ] Verificado logs no Streamlit Cloud
- [ ] Configurado alertas de erro

## 🔄 Atualizações Futuras

Para atualizar o app:
```bash
# Fazer alterações nos arquivos
git add .
git commit -m "Descrição da alteração"
git push
```

## 🆘 Em Caso de Problemas

1. Consulte o arquivo `DEPLOY.md` seção Troubleshooting
2. Verifique os logs no Streamlit Cloud
3. Confirme que todos os arquivos estão no GitHub
4. Verifique o `requirements.txt`
5. Teste localmente antes: `streamlit run app_obesity_prediction.py`

---

## 📞 Recursos Úteis

- **Documentação Streamlit:** https://docs.streamlit.io
- **Suporte GitHub:** https://docs.github.com
- **Streamlit Community:** https://discuss.streamlit.io

---

**Data do deploy:** ___/___/______
**Status:** ⬜ Planejado | ⬜ Em andamento | ⬜ Concluído | ⬜ Com problemas

**Notas:**
________________________________________________________________
________________________________________________________________
________________________________________________________________
