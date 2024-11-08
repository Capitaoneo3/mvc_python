import tkinter as tk

from controller.usuario_controller import UsuarioController
from controller.usuario_delete_controller import Usuario_delete_controller
from model.usuario_model import UsuarioModel
from view.usuario_delete_view import Usuario_delete_view
from view.usuario_view import UsuarioView


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = Usuario_delete_view(root)
    controller = Usuario_delete_controller(view, model)

    root.mainloop()
    model.fechar_conexao()