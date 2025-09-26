import ttkbootstrap as ttk
import tkinter as tk
from tkinter import Listbox
import tkinter.messagebox 
import sqlite3
class Menu_lista:
    def __init__(self):
#abrindo a janela
#fill aumenta ate as margens da tela e expand leva os itens a expandirem junto
      self.menu_lista = ttk.Window(themename="superhero",
                                    title="")
       
      self.menu_lista.geometry("1920x1080")


#tirulo
      self.titulo_lista = ttk.Label(self.menu_lista,
                                     text="Minha Lista De Tarefas",
                                     foreground="pink",
                                     font=("Times New Roman",30))
      self.titulo_lista.pack(pady=10)

  #frame para agrupar as coisas
      self.frame_inserir = ttk.Frame(self.menu_lista)
      self.frame_inserir.pack()

 
#caixa de texto que esta dentro do frame, o widht define o tamanho da caixa
      self.caixa_tarefa = ttk.Entry(self.frame_inserir, width=90)
      self.caixa_tarefa.pack(side="right")

#botao que tambem esta dentro o side define qual alado o ngc a parece
      self.botao_inserir = ttk.Button(self.frame_inserir, text="Adicionar", command= self.adicionando)
      self.botao_inserir.pack(side="left", padx=10, pady=(10))

#listbox

#criando a lista
      self.lista = tk.Listbox(self.menu_lista, width=70, height=20)  
      self.lista.pack(pady=20)

#frame para os botoes de baixo
      self.frame_final = ttk.Frame(self.menu_lista)
      self.frame_final.pack()

#botao excluir
      self.botao_excluir = ttk.Button(self.frame_final, text="Excluir", padding="10", command= self.excluir)
      self.botao_excluir.pack(side="left", padx=10, pady=10)

#botao concluir
      self.botao_concluir = ttk.Button(self.frame_final, text="Concluir", padding="10", command= self.concluir)
      self.botao_concluir.pack(side="right", padx=10, pady=10)

#botando as informações da caixa de texto na listbox
    def adicionando(self):
      self.texto = self.caixa_tarefa.get()
      self.lista.insert(tk.END, self.texto)  # adiciona a escrita no final da lista
      self.caixa_tarefa.delete(0, tk.END)  #para limpar a caixa de texto automaticamnete

#def para excluir a tarefa selecionada
    def excluir(self):
      self.selecionado = self.lista.curselection()  # pega o índice do item selecionado
      if self.selecionado:  # se algum item estiver selecionado
        self.lista.delete(self.selecionado[0])

      else:
        tk.messagebox.showerror(message="Selecione o item que quer excluir")

#def para marcar tarefa
    def concluir(self):
      self.conclu_selecionado= self.lista.curselection() #para selecionar a linha que quer concluir
      if self.conclu_selecionado:
        self.numero = self.conclu_selecionado[0] #pega o item por "numero"
        self.texto = self.lista.get(self.numero) #pega o texto para selecionar
        self.lista.delete(self.numero) #tira o texto antigo
        self.lista.insert(self.numero, self.texto + "✅") #poe o texto mas com o certinho
      else:
        tk.messagebox.showerror(message="Selecione o item que quer marcar como concluido")

#mantendo a janela rodando
    def run(self):
      self.menu_lista.mainloop()

if __name__ == "__main__":
    lista = Menu_lista()
    lista.run()
