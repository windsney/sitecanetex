import datetime
import tkinter

# email windsney@gmail.com
# In......@

# aula da hastag  parou 10:50completo F673/186  c.


from docx import Document
from docx.shared import Pt, Cm

import customtkinter as ctk

# Configura o estilo padrão
ctk.set_appearance_mode("light")  # "light", "dark", ou "system" para usar o tema do sistema
ctk.set_default_color_theme("blue")  # Definir o tema de cor: "blue", "dark-blue", "green"

# Função para criar a janela
def criar_janela():
    # Cria a janela principal
    janela = ctk.CTk()
    janela.title("Nome e Preço")

    # Definir o tamanho da janela
    janela.geometry("300x200")

    # Label e Entry para o nome do produto
    ctk.CTkLabel(janela, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    nome_entry = ctk.CTkEntry(janela)
    nome_entry.grid(row=0, column=1, padx=10, pady=10)

    # Label e Entry para o preço do produto
    ctk.CTkLabel(janela, text="Preço do Produto:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    preco_entry = ctk.CTkEntry(janela)
    preco_entry.grid(row=1, column=1, padx=10, pady=10)

    # Botão para fechar a janela
    fechar_button = ctk.CTkButton(janela, text="Fechar", command=janela.quit)
    fechar_button.grid(row=2, column=1, pady=20)

    # Inicia o loop da aplicação
    janela.mainloop()

# Chama a função para criar a janela
criar_janela()
