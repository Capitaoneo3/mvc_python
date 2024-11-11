import tkinter as tk

from controller.usuario_update_controller import Usuario_update_controller
from model.usuario_model import UsuarioModel
from view.usuario_update_view import Usuario_update_view




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = Usuario_update_view(root)
    controller = Usuario_update_controller(view, model)

    root.mainloop()
    model.fechar_conexao()