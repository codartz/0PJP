# ==========================================
# ATUALIZAR + ENVIAR ALTERAÇÕES
# ==========================================

# 1. Entrar na pasta
cd "C:\Users\Taís\OneDrive - SENAC-SC\Senac"

# 2. Ver mudanças
git status

# 3. Adicionar arquivos
git add .

# 4. Criar commit
git commit -m "Atualização"

# 5. Enviar para GitHub
git push origin main

# — alternativa para modificações em arquivos já versionados:
git commit -am "mensagem"   # combina add + commit
git push

# ==========================================
# COPIA E COLA
# ==========================================

git add . && git commit -m "atualização / "