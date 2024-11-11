import tkinter as tk
from tkinter import ttk
class Usuario_update_controller:
    def __init__(self, view:tk.Frame, model):
        self.view = view
        self.model = model
        self.carregar_usuarios()
        #self.deletar_bnt:ttk.Button =  self.view.deletar_button
        #self.deletar_bnt.config(command=self.deletar_user)
        self.view.atualizar_button.config(command = self.atualizar )
    def carregar_usuarios(self):
            usuarios = self.model.selecionar_usuarios()
            for usuario in usuarios:
                self.view.adicionar_usuario_lista(usuario)
    def atualizar(self):
        id = self.view.get_id()
        nome = self.view.get_nome()
        idade = self.view.get_idade()
       
        if self.model.atualiza_usuario(id,nome,idade):
            self.view.apagar_a_lista()
            self.carregar_usuarios()
            self.view.mostrar_aviso(f"o usuário foi atualizado!")
        else:
            self.view.mostrar_aviso(f"o usuário NÃO foi atualizado!")
