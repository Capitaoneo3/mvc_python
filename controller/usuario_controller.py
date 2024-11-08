import tkinter as tk
from tkinter import ttk
class UsuarioController:
    def __init__(self, view:tk.Frame, model):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.adicionar_usuario)
        
        self.carregar_usuarios()
        self.view.idade_entry.bind("<Return>", lambda event: self.adicionar_usuario())  # Corrigido para chamar o método
        self.view.idade_entry.focus()
        self.view.bind("<Return>", lambda event: self.adicionar_usuario())  # Corrigido para chamar o método
        self.view.focus()
        self.view.nome_entry.bind("<Return>", lambda event: self.adicionar_usuario())  # Corrigido para chamar o método
        self.view.nome_entry.focus()
    def adicionar_usuario(self):
        nome = self.view.get_nome()
        idade = self.view.get_idade()
        self.view.nome_entry.config(background="white")
        self.view.idade_entry.config(background="white")
        if not nome.isdigit() and nome and idade.isdigit():
            self.model.inserir_usuario(nome, int(idade))
            self.apagar_a_lista()
            self.carregar_usuarios()
            self.view.nome_entry.delete(0, tk.END)
            self.view.idade_entry.delete(0, tk.END)
        elif nome.isdigit() or nome == "":
            nome_entry:tk.Entry =  self.view.nome_entry
            nome_entry.config(background="red")
            self.view.mostrar_aviso("nome digitado errado.")

        elif not idade.isdigit() or idade:
            idade_entry:tk.Entry =  self.view.idade_entry
            idade_entry.config(background="red")
            self.view.mostrar_aviso("idade digitada errada.")

        else:
            idade_entry:tk.Entry =  self.view.idade_entry
            idade_entry.config(background="red") 
            idade_entry:tk.Entry =  self.view.idade_entry
            idade_entry.config(background="red")
            self.view.mostrar_aviso("Calma lá, você não preencheu os campos corretamente meu nobre.")
    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)

    def apagar_a_lista(self):
        self.view.usuarios_listbox.delete(0,tk.END)