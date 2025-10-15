import tkinter as tk
from tkinter import ttk, messagebox

# Função para adicionar usuário à lista
def adicionar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    genero = genero_var.get()
    linguagem = linguagem_var.get()
    
    if not nome or not email:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    
    # Adiciona as informações na lista de visualização
    lista_usuarios.insert('', 'end', values=(nome, email, genero, linguagem))
    
    # Limpa os campos após o cadastro
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    genero_var.set('Selecione')
    linguagem_var.set('Selecione')

# Função para remover usuário selecionado
def remover_usuario():
    selecionado = lista_usuarios.selection()
    if selecionado:
        lista_usuarios.delete(selecionado)
    else:
        messagebox.showwarning("Atenção", "Por favor, selecione um usuário para remover!")
        
# Função para exibir quantidade de usuários cadastrados
def exibir_total_usuarios():
    total = len(lista_usuarios.get_children())
    messagebox.showinfo("Total de Usuários", f"Total de Usuários Cadastrados: {total}")
    
# Criação da Janela Principal
root = tk.Tk()
root.title("Sistema de Cadastro de Usuários")
root.geometry("600x400")

# Frame para os Campos de entrada
frame_formulario = tk.Frame(root, padx=20, pady=10)
frame_formulario.pack(pady=10)

# Campo de Nome
label_nome = tk.Label(frame_formulario, text="Nome:")
label_nome.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_nome = tk.Entry(frame_formulario)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

# Campo do email
label_email = tk.Label(frame_formulario, text="Email:")
label_email.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_email = tk.Entry(frame_formulario)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# Campo de Seleção de Gênero
label_genero = tk.Label(frame_formulario, text="Gênero:")
label_genero.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
genero_var = tk.StringVar()
genero_var.set('Selecione')
combo_genero = ttk.Combobox(frame_formulario, textvariable=genero_var, state='readonly', values=["Masculino", "Feminino", "Outro"])
combo_genero.grid(row=2, column=1, padx=5, pady=5)

# Campo de Seleção de Linguagem Preferida
label_linguagem = tk.Label(frame_formulario, text="Linguagem de Programação:")
label_linguagem.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
linguagem_var = tk.StringVar()
linguagem_var.set('Selecione')
combo_linguagem = ttk.Combobox(frame_formulario, textvariable=linguagem_var, state='readonly', values=["Python", "Java", "C++", "JavaScript"])
combo_linguagem.grid(row=3, column=1, padx=5, pady=5)

# Botão de Adicionar Usuário
btn_adicionar = tk.Button(frame_formulario, text="Adicionar Usuário", command=adicionar_usuario)
btn_adicionar.grid(row=4, columnspan=2, pady=10)

# Frame para visualização da Lista de Usuários
frame_lista = tk.Frame(root, padx=10, pady=10)
frame_lista.pack(pady=10)

# Tabela de Visualização de Usuários
colunas = ("Nome", "Email", "Gênero", "Linguagem Preferida")
lista_usuarios = ttk.Treeview(frame_lista, columns=colunas, show="headings")
for coluna in colunas:
    lista_usuarios.heading(coluna, text=coluna)
    lista_usuarios.column(coluna, minwidth=0, width=150, stretch=tk.NO)
    
# Adiciona uma Barra de Rolagem
scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=lista_usuarios.yview)
lista_usuarios.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Exibe a Tabela
lista_usuarios.pack()

# Frame para os botões de Ação
frame_acoes = tk.Frame(root, padx=10, pady=10)
frame_acoes.pack(pady=10)

# Botão para Remover Usuário
btn_remover = tk.Button(frame_acoes, text="Total de Usuário", command=remover_usuario)
btn_remover.grid(row=0, column=0, padx=10)

# Botão para Exibir Usuários
btn_total = tk.Button(frame_acoes, text="Total de Usuários", command=exibir_total_usuarios)
btn_total.grid(row=0, column=1, padx=10)

# Inicia o Loop Principal da Interface
root.mainloop()