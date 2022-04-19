import sqlite3

conn = sqlite3.connect('crud.db')

cursor = conn.cursor()

def cria_tabela():
    cursor.execute('''
        CREATE TABLE USUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, EMAIL TEXT, ENDERECO TEXT)
    ''')

    conn.commit()
    conn.close()

def insere_dados(nome, email, endereco):
    cursor.execute('''
        INSERT INTO USUARIOS (NOME, EMAIL, ENDERECO) VALUES (?, ?, ?)
    ''', (nome, email, endereco))

    conn.commit()
    conn.close()

def deleta_banco():
    cursor.execute(
        ''' DROP TABLE USUARIOS '''
    )
    conn.commit()
    conn.close()