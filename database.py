import sqlite3
from contextlib import contextmanager

DATABASE = 'data/laticinios.db'

@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with open('schema.sql') as f:
        sql_commands = f.read()
    with get_db() as conn:
        conn.executescript(sql_commands)
        conn.commit()

def add_area(nome, descricao):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO areas_armazem (nome, descricao) VALUES (?, ?)', (nome, descricao))
        conn.commit()
        return cursor.lastrowid

def get_all_areas():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM areas_armazem')
        return [dict(row) for row in cursor.fetchall()]

def get_area_by_id(area_id):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM areas_armazem WHERE id = ?', (area_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

def update_areas(area_id, nome, descricao):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE areas_armazem SET nome = ?, descricao = ? WHERE id = ?', (nome, descricao, area_id))
        conn.commit()
        return cursor.rowcount > 0

def delete_areas(area_id):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM areas_armazem WHERE id = ?', (area_id,))
        conn.commit()
        return cursor.rowcount > 0