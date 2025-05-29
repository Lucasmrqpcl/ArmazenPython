import sqlite3

import os
from werkzeug.security import generate_password_hash, check_password_hash


# definir caminho para bd
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'laticinios')


def get_db_connection():
    os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row # Permite acessar colunas pelo nome (ex: row['nome'])
    return conn


def init_db():
#Inicializa o banco de dados usando o schema.sql.
    conn = get_db_connection()
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

# --- Funções para Usuários ---
def create_user(username, password, role='user'):
#Cria um novo usuário com senha hasheada."""
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, generate_password_hash(password), role)
            )
        conn.commit()
    except sqlite3.IntegrityError: # Caso o username já exista
        conn.close()
    return False # Indica falha
    conn.close()
    return True # Indica sucess

def get_user_by_username(username):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close
    return user


def check_user_password(username, password):
    user = get_user_by_username()
    if user and check_password_hash(user['password_hash'], password):
        return user
    return None


def add_area(nome, descricao=''):
    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO areas_armazem (nome, descricao) VALUES (?, ?)", (nome, descricao)) 
    except sqlite3.IntegrityError:      
        conn.close()    
        return False # Indica falha
    conn.close()
    return True # Indica sucesso

def get_all_areas():
    conn = get_db_connection()
    areas = conn.execute("SELECT * FROM areas_armazem ORDER BY nome").fetchall()
    conn.close
    return areas

def get_area_by_id(area_id):
    conn = get_db_connection()
    area = conn.execute("SELECT * FROM areas_armazem WHERE id = ?", (area_id,)).fetchone()
    conn.close
    return area

def update_area(area_id, nome, descricao):
    conn = get_db_connection()
    try:
        conn.execute("UPDATE areas_armazem SET nome = ?, descricao = ?  WHERE id = ?", (nome, descricao, area_id)) 
    except sqlite3.IntegrityError:      
        conn.close()    
        return False # Indica falha
    conn.close()
    return True # Indica sucesso

def delete_area(area_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM areas_armazem WHERE id = ?", (area_id,))
    conn.commit()
    conn.close()


    
