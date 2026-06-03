"""
╔════════════════════════════════════════════════════════════════════════════╗
║            ATIVIDADE PRÁTICA - COMANDOS SQL (DDL)                          ║
║                                                                            ║
║  Objetivo: Praticar a escrita e estrutura dos comandos SQL, com base       ║
║  no conteúdo estudado em aula.                                             ║
║                                                                            ║
║  Nota: Esta atividade pode ser realizada sem utilização de MySQL           ║
║  Workbench, DBeaver, One Compiler e outros.                                ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. CRIAÇÃO DE BANCO DE DADOS
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Escreva o comando SQL para criar um banco de dados chamado 'biblioteca'.
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 2. SELEÇÃO DO BANCO DE DADOS
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Após criar o banco 'biblioteca', escreva o comando SQL utilizado para
# selecioná-lo.
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 3. CRIAÇÃO DA TABELA LIVROS
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Crie uma tabela chamada 'livros' contendo os seguintes campos:
#   • id_livro       (inteiro, chave primária, autoincremental)
#   • titulo         (texto com até 150 caracteres, obrigatório)
#   • autor          (texto com até 200 caracteres)
#   • ano_publicacao (inteiro)
#   • disponivel     (verdadeiro ou falso)
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 4. CRIAÇÃO DA TABELA USUARIOS
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Crie uma tabela chamada 'usuarios' com os seguintes campos:
#   • id_usuario (inteiro, chave primária, auto incremento)
#   • nome       (texto com até 100 caracteres, obrigatório)
#   • sobrenome  (texto com até 100 caracteres, obrigatório)
#   • email      (texto com até 120 caracteres, único e obrigatório)
#   • senha      (texto com até 60 caracteres, obrigatório)
#   • ativo      (verdadeiro ou falso)
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 5. CRIAÇÃO DA TABELA CLIENTES
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Crie uma tabela chamada 'clientes' contendo os seguintes campos:
#   • id_cliente       (inteiro, chave primária, auto incremento)
#   • nome             (texto com até 100 caracteres, obrigatório)
#   • cpf              (texto com tamanho fixo de 11 caracteres, único)
#   • telefone         (texto com até 15 caracteres)
#   • data_nascimento  (data)
#   • ativo            (verdadeiro ou falso)
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 6. CRIAÇÃO DA TABELA PRODUTOS
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Crie uma tabela chamada 'produtos' contendo os seguintes campos:
#   • id_produto    (inteiro, chave primária, auto incremento)
#   • nome          (texto com até 80 caracteres, obrigatório)
#   • descricao     (texto longo)
#   • preco         (número decimal com duas casas decimais)
#   • estoque       (inteiro)
#   • data_cadastro (data e hora)
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 7. INTERPRETAÇÃO DE COMANDOS (SQL)
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Explique, com suas próprias palavras, o que faz o comando SQL abaixo:
#
#   CREATE TABLE pedidos (
#       id_pedido INT AUTO_INCREMENT PRIMARY KEY,
#       data_pedido DATETIME,
#       valor_total DECIMAL(10,2) NOT NULL,
#       status VARCHAR(20) DEFAULT 'PENDENTE'
#   );
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 8. IDENTIFICAÇÃO DE ERROS
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Analise o SQL abaixo e identifique os erros presentes:
#
#   CREATE TABLE funcionarios (
#       id INT AUTO_INCREMENT,
#       nome VARCHAR(100) NOT NULL,
#       salario DECIMAL(10,2),
#   );
#
# Resposta:


# ═══════════════════════════════════════════════════════════════════════════
# 9. CRIAÇÃO LIVRE
# ═══════════════════════════════════════════════════════════════════════════
# Enunciado:
# Crie uma tabela chamada 'agendamentos' contendo no mínimo 7 campos,
# respeitando os seguintes critérios:
#   ✓ Uma chave primária
#   ✓ Uma chave única
#   ✓ Uma chave estrangeira
#   ✓ Um campo autoincremental
#   ✓ Um campo de data
#   ✓ Um campo numérico
#   ✓ Um campo obrigatório
#
# Resposta: