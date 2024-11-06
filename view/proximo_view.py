import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ProximoView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
   
    def create_widgets(self):
        self.texto = tk.Label(self, text="Nova página")
        self.texto.pack(fill="both",expand=True)


