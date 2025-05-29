-- Remove tabelas existentes para começar do zero (cuidado em produção!)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS areas_armazem;
DROP TABLE IF EXISTS produtos_catalogo;
DROP TABLE IF EXISTS produtos_areas;
-- Tabela de Usuários
CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador único, auto-incrementado
 username TEXT UNIQUE NOT NULL, -- Nome de usuário, deve ser único e não pode ser vazio
 password_hash TEXT NOT NULL, -- Senha (armazenada como hash seguro, não texto puro!)
role TEXT NOT NULL DEFAULT 'user' -- Cargo/Permissão (ex: 'user', 'admin', 'manager')
);
-- Tabela de Áreas de Armazenamento
CREATE TABLE areas_armazem (
id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL UNIQUE, -- Nome da área, deve ser único
 descricao TEXT
);
-- Tabela de Produtos do Catálogo
CREATE TABLE produtos_catalogo (
id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL UNIQUE, -- Nome do produto no catálogo, deve ser único
 tipo TEXT, -- Tipo ou categoria do produto
 descricao TEXT
);
-- Tabela de Produtos nas Áreas (relaciona áreas com produtos do catálogo)
CREATE TABLE produtos_areas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
 area_id INTEGER NOT NULL, -- Chave estrangeira para a tabela areas_armazem
 produto_catalogo_id INTEGER NOT NULL, -- Chave estrangeira para a tabela produtos_catalogo
 quantidade INTEGER NOT NULL DEFAULT 0,
 data_validade DATE, -- Formato: YYYY-MM-DD
 lote TEXT,
FOREIGN KEY (area_id) REFERENCES areas_armazem (id),
FOREIGN KEY (produto_catalogo_id) REFERENCES produtos_catalogo (id)
);

-- Dados iniciais (opcional, para teste)
-- Inserindo um usuário administrador (senha 'admin' - NUNCA FAÇA ISSO EM PRODUÇÃO REAL)
-- Para gerar um hash seguro, usaríamos bibliotecas Python, aqui é só um exemplo de placeholder
INSERT INTO users (username, password_hash, role) VALUES ('admin', 'pbkdf2:sha256:...', 'admin');
INSERT INTO users (username, password_hash, role) VALUES ('gerente', 'pbkdf2:sha256:...',
'manager');
-- Inserindo algumas áreas de exemplo
INSERT INTO areas_armazem (nome, descricao) VALUES ('Câmara Fria 01',
'Produtos que necessitam de refrigeração intensa.');
INSERT INTO areas_armazem (nome, descricao) VALUES ('Prateleira Secos A', 'Produtos não
perecíveis.');
-- Inserindo alguns produtos no catálogo de exemplo
INSERT INTO produtos_catalogo (nome, tipo, descricao) VALUES ('Iogurte Natural Copo', 'Iogurte',
'Iogurte natural integral em copo de 170g.');
INSERT INTO produtos_catalogo (nome, tipo, descricao) VALUES ('Queijo Minas Frescal', 'Queijo',
'Queijo minas frescal artesanal, peça de aproximadamente 500g.');
INSERT INTO produtos_catalogo (nome, tipo, descricao) VALUES ('Leite Integral UHT', 'Leite',
'Leite longa vida integral, caixa de 1L.');
