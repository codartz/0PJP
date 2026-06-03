Renomear ficheiros
Tenha cuidado para não re-renomear arquivos que já têm extensão – verifique a pasta primeiro com dir/Get-ChildItem.

# renomeia um único ficheiro
ren "nome-do-arquivo" "nome-do-arquivo.py"

# renomeia todos os arquivos que não têm extensão, acrescentando .py
Get-ChildItem -File |
  Where-Object { -not $_.Extension } |
  Rename-Item -NewName { "$($_.Name).py" }

# --- renomeia todos os arquivos SEM extensão na pasta actual ---
Get-ChildItem -File |
    Where-Object { -not $_.Extension } |
    Rename-Item -NewName { "$($_.Name).py" }

# exemplo específico para cada pasta:
cd "c:\Users\Taís\OneDrive - SENAC-SC\Senac\ \ "
Get-ChildItem -File |
    Where-Object { -not $_.Extension } |
    Rename-Item -NewName { "$($_.Name).py" }

cd "c:\Users\Taís\OneDrive - SENAC-SC\Senac\ \ "
Get-ChildItem -File |
    Where-Object { -not $_.Extension } |
    Rename-Item -NewName { "$($_.Name).py" }

# ==========================================
# RENOMEAR ARQUIVOS PARA .PY
# ==========================================

# IMPORTANTE:
# Verifique antes se os arquivos já têm extensão
# Evita renomear arquivos errado

# 1. Listar arquivos (verificar)
Get-ChildItem -File
``

# 2. renomeia um único ficheiro
ren "nome-do-arquivo" "nome-do-arquivo.py"

# 3. renomeia todos os arquivos que não têm extensão, acrescentando .py
Get-ChildItem -File |
  Where-Object { -not $_.Extension } |
  Rename-Item -NewName { "$($_.Name).py" }

# 4. renomeia todos os arquivos SEM extensão na pasta actual ---
cd "c:\Users\Taís\OneDrive - SENAC-SC\ \ \ "
Get-ChildItem -File |
    Where-Object { -not $_.Extension } |
    Rename-Item -NewName { "$($_.Name).py" }

