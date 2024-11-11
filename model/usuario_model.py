import sqlite3

class UsuarioModel:
    def __init__(self, db_name='exemplo.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER
            )
        ''')
        self.conn.commit()

    def inserir_usuario(self, nome, idade):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, idade)
            VALUES (?, ?)
        ''', (nome, idade))
        self.conn.commit()

    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()


    def atualiza_usuario(self,id,nome,idade):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'''
                update usuarios
                set nome = ?,idade = ?
                where id = ?
            ''',(nome,idade,id))
            self.conn.commit()
            return True
        except Exception as e:   
            print(f"Error deleting user: {e}")
            self.conn.rollback()
            return False 

    def delete_usuario(self, id):
        cursor = self.conn.cursor()

        try:
            cursor.execute(f"DELETE FROM usuarios WHERE id = ?", (id,))
            self.conn.commit()
            return True  # Deletion successful
        except Exception as e:
            print(f"Error deleting user: {e}")
            self.conn.rollback()
            return False  # Deletion failed

    def select_usuario(self,id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios where id = ?',(id,))
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()



