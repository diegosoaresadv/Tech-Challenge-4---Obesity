# 🔧 Comandos Git Úteis para o Projeto

Este documento contém os comandos Git mais úteis para gerenciar seu projeto.

## 📚 Configuração Inicial

### Configurar identidade do Git (primeira vez)
```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu.email@exemplo.com"
```

### Verificar configuração
```bash
git config --list
```

## 🚀 Primeiro Deploy

### Inicializar repositório
```bash
cd pasta-do-projeto
git init
```

### Adicionar todos os arquivos
```bash
git add .
```

### Fazer primeiro commit
```bash
git commit -m "Initial commit: Obesity prediction app"
```

### Conectar ao GitHub
```bash
# Substitua SEU-USUARIO pelo seu username do GitHub
git remote add origin https://github.com/SEU-USUARIO/obesity-prediction.git
```

### Verificar remote
```bash
git remote -v
```

### Renomear branch para main
```bash
git branch -M main
```

### Enviar para GitHub
```bash
git push -u origin main
```

## 🔄 Atualizações Subsequentes

### Ver status dos arquivos
```bash
git status
```

### Adicionar arquivo específico
```bash
git add app_obesity_prediction.py
```

### Adicionar todos os arquivos modificados
```bash
git add .
```

### Fazer commit com mensagem descritiva
```bash
git commit -m "Descrição clara da mudança"
```

### Enviar para GitHub
```bash
git push
```

### Fluxo completo de atualização
```bash
git add .
git commit -m "Update: descrição da mudança"
git push
```

## 📥 Baixar Atualizações

### Baixar atualizações do GitHub
```bash
git pull
```

### Baixar sem merge automático
```bash
git fetch
```

## 🌿 Trabalhando com Branches

### Criar nova branch
```bash
git branch nome-da-feature
```

### Mudar para outra branch
```bash
git checkout nome-da-feature
```

### Criar e mudar para nova branch
```bash
git checkout -b nome-da-feature
```

### Listar todas as branches
```bash
git branch -a
```

### Voltar para branch main
```bash
git checkout main
```

### Fazer merge de uma branch
```bash
git checkout main
git merge nome-da-feature
```

### Deletar branch local
```bash
git branch -d nome-da-feature
```

## 📜 Histórico e Logs

### Ver histórico de commits
```bash
git log
```

### Ver histórico resumido
```bash
git log --oneline
```

### Ver últimos 5 commits
```bash
git log -5
```

### Ver diferenças
```bash
git diff
```

## ↩️ Desfazer Mudanças

### Desfazer mudanças em arquivo não commitado
```bash
git checkout -- nome-do-arquivo.py
```

### Remover arquivo do staging (antes do commit)
```bash
git reset HEAD nome-do-arquivo.py
```

### Desfazer último commit (mantendo alterações)
```bash
git reset --soft HEAD~1
```

### Desfazer último commit (descartando alterações)
```bash
git reset --hard HEAD~1
```

## 🏷️ Tags e Releases

### Criar tag
```bash
git tag -a v1.0.0 -m "Primeira versão estável"
```

### Listar tags
```bash
git tag
```

### Enviar tag para GitHub
```bash
git push origin v1.0.0
```

### Enviar todas as tags
```bash
git push --tags
```

## 🔍 Informações e Diagnóstico

### Ver configuração do repositório
```bash
git config --list
```

### Ver remote URLs
```bash
git remote -v
```

### Ver branch atual
```bash
git branch --show-current
```

### Verificar tamanho do repositório
```bash
git count-objects -vH
```

## 🚨 Comandos de Emergência

### Forçar push (use com cuidado!)
```bash
git push --force
```

### Limpar arquivos não rastreados
```bash
git clean -fd
```

### Resetar para estado do GitHub
```bash
git fetch origin
git reset --hard origin/main
```

## 📦 Trabalhando com Arquivos Grandes

### Instalar Git LFS
```bash
git lfs install
```

### Rastrear arquivos grandes (ex: .joblib)
```bash
git lfs track "*.joblib"
```

### Adicionar arquivo .gitattributes
```bash
git add .gitattributes
```

### Verificar arquivos LFS
```bash
git lfs ls-files
```

## 🎯 Dicas Práticas

### Mensagens de commit efetivas
```bash
# Boas práticas:
git commit -m "Add: Nova funcionalidade X"
git commit -m "Fix: Corrige erro no cálculo do IMC"
git commit -m "Update: Melhora visualização dos gráficos"
git commit -m "Remove: Código obsoleto de validação"
git commit -m "Refactor: Reorganiza estrutura de funções"
```

### Verificar antes de commitar
```bash
git status          # Ver o que mudou
git diff            # Ver detalhes das mudanças
git add .           # Adicionar tudo
git status          # Confirmar o que será commitado
git commit -m "..."  # Fazer commit
```

### Workflow completo recomendado
```bash
# 1. Verificar estado
git status

# 2. Baixar atualizações (se trabalhando em equipe)
git pull

# 3. Fazer suas alterações nos arquivos...

# 4. Ver o que mudou
git status
git diff

# 5. Adicionar arquivos
git add .

# 6. Commitar
git commit -m "Descrição clara das mudanças"

# 7. Enviar para GitHub
git push

# 8. Verificar no GitHub se tudo está correto
```

## 🆘 Resolver Problemas Comuns

### Erro: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/SEU-USUARIO/obesity-prediction.git
```

### Erro: "Authentication failed"
```bash
# Se usar 2FA no GitHub, crie um Personal Access Token:
# GitHub > Settings > Developer settings > Personal access tokens
# Use o token como senha
```

### Erro: "Updates were rejected"
```bash
git pull --rebase
git push
```

### Conflitos de merge
```bash
# 1. Abra os arquivos com conflito
# 2. Resolva os conflitos manualmente
# 3. Adicione os arquivos resolvidos
git add .
git commit -m "Resolve merge conflicts"
git push
```

## 📝 Notas Importantes

- Sempre faça `git status` antes de commits importantes
- Nunca use `--force` sem ter certeza
- Commits pequenos e frequentes são melhores que commits grandes
- Escreva mensagens de commit descritivas e claras
- Teste localmente antes de fazer push
- Mantenha o `.gitignore` atualizado

## 🔗 Recursos Adicionais

- **Documentação Git:** https://git-scm.com/doc
- **GitHub Docs:** https://docs.github.com
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **Pro Git Book:** https://git-scm.com/book/pt-br/v2

---

**Mantenha este arquivo como referência rápida! 📖**
