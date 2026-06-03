# ============================================
# CENÁRIO GAMIFICADO — SISTEMA ACADÊMICO PERDIDO
# ============================================

# A faculdade DataVerse precisa reconstruir seu sistema acadêmico.
# Os agentes (alunos) devem analisar os dados e responder perguntas investigativas usando JOINs.

# ============================================
# OBJETIVO
# ============================================

# Criar o banco e as tabelas principais.


# ============================================
# MISSÃO
# ============================================

# Crie o esquema da universidade.


# ============================================
# ENTIDADE: CURSO
# ============================================

# Campos sugeridos:
# id_curso -> identificador (PK)
# nome_curso -> texto
# modalidade -> texto (Presencial / EAD)
# carga_horaria -> número
# status -> texto (Ativo / Inativo)

# Dados:

# id | nome               | modalidade | carga | status
# 1  | ADS                | Presencial | 2000  | Ativo
# 2  | Engenharia         | Presencial | 3000  | Ativo
# 3  | Design             | EAD        | 1800  | Ativo
# 4  | Jogos Digitais     | EAD        | 2200  | Ativo
# 5  | Ciência de Dados   | EAD        | 2400  | Inativo


# ============================================
# ENTIDADE: ALUNO
# ============================================

# Campos sugeridos:
# id_aluno -> PK
# nome_aluno -> texto
# idade -> número
# cidade -> texto
# id_curso -> FK (pode ser NULL)
# status_matricula -> texto (Ativo / Trancado)

# Dados:

# id | nome     | idade | cidade         | id_curso | status
# 1  | Ana      | 20    | Palhoça        | 1        | Ativo
# 2  | Carlos   | 22    | São José       | 1        | Ativo
# 3  | Marina   | 25    | Florianópolis  | 2        | Ativo
# 4  | João     | 19    | Palhoça        | NULL     | Ativo
# 5  | Fernanda | 30    | Biguaçu        | 3        | Trancado
# 6  | Lucas    | 28    | São José       | 99       | Ativo


# ============================================
# ENTIDADE: MATRICULA (TABELA DE RELAÇÃO)
# ============================================

# Campos sugeridos:
# id_matricula -> PK
# id_aluno -> FK
# id_curso -> FK
# data_matricula -> data
# status_matricula -> ativo/cancelado/concluído
# nota_final -> número

# Dados:

# id | aluno | curso | data       | status     | nota
# 1  | 1     | 1     | 2024-02-01 | Ativo      | 8.5
# 2  | 1     | 3     | 2024-02-10 | Ativo      | 9.0
# 3  | 2     | 1     | 2024-02-01 | Ativo      | 7.0
# 4  | 3     | 2     | 2024-02-03 | Ativo      | 8.0
# 5  | 4     | 4     | 2024-03-01 | Cancelado  | NULL
# 6  | 5     | 3     | 2024-01-15 | Concluído  | 9.5
# 7  | 6     | 2     | 2024-02-20 | Ativo      | 6.5
# 8  | 6     | 4     | 2024-03-10 | Ativo      | 7.5


# ============================================
# PERGUNTAS — INNER JOIN
# ============================================

# - Quais alunos estão matriculados em cursos?
# - Liste aluno + curso + nota.
# - Quais cursos possuem alunos ativos?
# - Quem está matriculado em mais de um curso?


# ============================================
# PERGUNTAS — LEFT JOIN (ALUNO → MATRICULA)
# ============================================

# - Liste TODOS os alunos e seus cursos.
# - Quais alunos nunca se matricularam?
# - Quem não possui vínculo acadêmico?


# ============================================
# PERGUNTAS — LEFT JOIN (CURSO → MATRICULA)
# ============================================

# - Quais cursos não possuem alunos?
# - Existem cursos inativos sem matrícula?
