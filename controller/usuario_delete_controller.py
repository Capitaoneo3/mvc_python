import tkinter as tk
from tkinter import ttk
class Usuario_delete_controller:
    def __init__(self, view:tk.Frame, model):
        self.view = view
        self.model = model
        self.carregar_usuarios()

    def carregar_usuarios(self):
            usuarios = self.model.selecionar_usuarios()
            for usuario in usuarios:
                self.view.adicionar_usuario_lista(usuario)
