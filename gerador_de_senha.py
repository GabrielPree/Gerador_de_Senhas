import tkinter as tk
from tkinter import messagebox
import random
import string

# Funções
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
    except ValueError:
        messagebox.showerror("[Erro]", "Digite um número válido para o tamanho da senha.")
        return

    caracteres = ""
    if maiusculas.get():
        caracteres += string.ascii_uppercase
    if minusculas.get():
        caracteres += string.ascii_lowercase
    if numeros.get():
        caracteres += string.digits
    if simbolos.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Aviso", "Selecione pelo menos uma opção de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)


    forca_texto, cor = avaliar_forca(senha)
    forca_senha.config(text=f"Força da senha: {forca_texto}", fg=cor)

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
    else:
        messagebox.showwarning("Aviso", "Não há senha para copiar!")

# avaliando a força da senha para gerar um texto e mudar a cor do texto
def avaliar_forca(senha):
    tipos = 0
    if any(c.isupper() for c in senha):
        tipos += 1
    if any(c.islower() for c in senha):
        tipos += 1
    if any(c.isdigit() for c in senha):
        tipos += 1
    if any(c in string.punctuation for c in senha):
        tipos += 1

    if len(senha) < 6 or tipos == 1:
        return "Fraca", "red"
    elif len(senha) <= 10 or tipos == 2:
        return "Média", "orange"
    else:
        return "Forte", "green"

# Hover para os botões
def on_enter(e, btn, hover_color):
    btn['background'] = hover_color

def on_leave(e, btn, default_color):
    btn['background'] = default_color

# Janela principal do tkinter
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("450x400")
janela.resizable(False, False)

# Fontes e cores dos botões
fonte_titulo = ("Tahoma", 14, "bold")
fonte_texto = ("Helvetica", 12)
fonte_botao = ("Helvetica", 12, "bold")
cor_gerar = "#26B7CA"
cor_copiar = "#6B21F3"
cor_hover_gerar = "#208F9E"
cor_hover_copiar = "#5C2BB8"

# frame do tamanho da palavra
frame_tamanho = tk.Frame(janela)
frame_tamanho.pack(pady=10)

tk.Label(frame_tamanho, text="Tamanho da senha:", font=fonte_titulo).pack(side="left")
entry_tamanho = tk.Entry(frame_tamanho, width=5, font=fonte_texto, justify="center")
entry_tamanho.pack(side="left", padx=5)

# frame com checkbox para as opções
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack(pady=10)

maiusculas = tk.BooleanVar()
minusculas = tk.BooleanVar()
numeros = tk.BooleanVar()
simbolos = tk.BooleanVar()

tk.Checkbutton(frame_opcoes, text="Letras maiúsculas (A-Z)", variable=maiusculas, font=fonte_texto).pack(anchor="center", pady=2)
tk.Checkbutton(frame_opcoes, text="Letras minúsculas (a-z)", variable=minusculas, font=fonte_texto).pack(anchor="center", pady=2)
tk.Checkbutton(frame_opcoes, text="Números (0-9)", variable=numeros, font=fonte_texto).pack(anchor="center", pady=2)
tk.Checkbutton(frame_opcoes, text="Símbolos (!@#$...)", variable=simbolos, font=fonte_texto).pack(anchor="center", pady=2)

# Botão para gerar a senha
frame_gerar = tk.Frame(janela)
frame_gerar.pack(pady=10)

btn_gerar = tk.Button(frame_gerar, text="Gerar Senha", command=gerar_senha, font=fonte_botao, width=20, bg=cor_gerar, fg="white", relief="flat")
btn_gerar.pack()
btn_gerar.bind("<Enter>", lambda e: on_enter(e, btn_gerar, cor_hover_gerar))
btn_gerar.bind("<Leave>", lambda e: on_leave(e, btn_gerar, cor_gerar))

# frame para exibir a senha
frame_resultado = tk.Frame(janela)
frame_resultado.pack(pady=10)

entry_resultado = tk.Entry(frame_resultado, width=40, font=fonte_texto, justify="center")
entry_resultado.pack(pady=10)

# Botão para copiar a senha
btn_copiar = tk.Button(frame_resultado, text="Copiar Senha", command=copiar_senha, font=fonte_botao, width=20, bg=cor_copiar, fg="white", relief="flat")
btn_copiar.pack(pady=5)
btn_copiar.bind("<Enter>", lambda e: on_enter(e, btn_copiar, cor_hover_copiar))
btn_copiar.bind("<Leave>", lambda e: on_leave(e, btn_copiar, cor_copiar))

# Força da senha
forca_senha = tk.Label(frame_resultado, font=fonte_texto)
forca_senha.pack(pady=5)

# Inicia interface e mantem o loop
janela.mainloop()