import tkinter as tk
from tkinter import ttk
class Usuario_delete_controller:
    def __init__(self, view:tk.Frame, model):
        self.view = view
        self.model = model
        self.carregar_usuarios()
        self.deletar_bnt:ttk.Button =  self.view.deletar_button
        self.deletar_bnt.config(command=self.deletar_user)
    def carregar_usuarios(self):
            usuarios = self.model.selecionar_usuarios()
            for usuario in usuarios:
                self.view.adicionar_usuario_lista(usuario)
    def deletar_user(self):
        self.id_user = self.view.get_id()
       
        
        if self.id_user == "":
            self.view.mostrar_aviso(f"Favor digitar id primeiro.")
        else:
            self.model.delete_usuario(self.id_user)
            self.view.apagar_a_lista()
            self.carregar_usuarios()
            self.view.id_entry.delete(0, tk.END)