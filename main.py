import tkinter as tk

from controller.usuario_controller import UsuarioController
from model.usuario_model import UsuarioModel
from view.usuario_view import UsuarioView


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = UsuarioView(root)
    controller = UsuarioController(view, model)

    root.mainloop()
    model.fechar_conexao()