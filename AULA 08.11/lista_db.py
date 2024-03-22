
import os
import sqlite3

class Lista():
    def __init__(self):
        
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute( '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
        ''')

    def connect(self):
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()


    def finalizar(self):
        self.conn.commit() 
        self.conn.close()
        
    
    def Inserir(self):
        self.connect()
        nome = input('Digite o Nome:')
        idade = int(input('Digite a Idade:'))
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        self.finalizar()
    
    def listar(self):
        self.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM usuarios")
        self.registros = self.cursor.fetchall()
        for item in self.registros:
            print(f"ID: {item[0]}, Nome: {item[1]}, Idade: {item[2]}")
    
        self.finalizar()
    
    def remover(self):
        self.connect()
        id = int(input('Digite o id:'))
        self.cursor = self.conn.cursor()
        self.cursor.execute(f'DELETE FROM usuarios WHERE id={id}')
        self.finalizar()
    
    def editar(self):
        self.connect()
        id = int(input('Digite o id:'))
        novonome = input('Digite o novo Nome:')
        novaidade = int(input("Digite a Idade:"))
        self.cursor.execute(f"UPDATE usuarios SET nome='{novonome}', idade='{novaidade}' WHERE id='{id}'")
        self.finalizar()
