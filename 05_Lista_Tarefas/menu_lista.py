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
       
      #tamanho da tela
      self.menu_lista.geometry("1920x1080")

      
      #titulo
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

#######################################################################################################################################
      conexao = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")

      #cursor responsavel pelo banoc de dados
      cursor = conexao.cursor()

      
      #criando as informações da tabela
      #para criar tabela
      sql_criar_tabela = """
                              CREATE TABLE IF NOT EXISTS tarefa (
                              codigo integer primary key autoincrement, 
                              descricao_tarefa varchar(200)
                              );
                              """
      #para executar a tabela
      cursor.execute(sql_criar_tabela)
      conexao.commit()

      #para fechar o cursor
      cursor.close()
      conexao.close()

      self.atualizar_lista()
     
#######################################################################################################################################
      #cursor responsavel pelo banoc de dados
      conexao_select = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")

      cursor_select = conexao_select.cursor()

      #criando as informações da tabela
      sql_select_tabela = """
                          SELECT codigo, descricao_tarefa FROM tarefa;
                              """
      #para executar a tabela

      cursor_select.execute(sql_select_tabela)
      lista_de_tarefas = cursor_select.fetchall()

      #para fechar o cursor
      cursor_select.close()
      conexao_select.close()

      for linha in lista_de_tarefas:
        self.lista.insert("end",linha[1])


    def atualizar_lista(self):
      #esse é para fazr um select
      conexao_select = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")



##########################################################################################################################################

#botando as informações da caixa de texto na listbox
    def adicionando(self):
      self.texto = self.caixa_tarefa.get()
      self.lista.insert(tk.END, self.texto)  # adiciona a escrita no final da lista
      self.caixa_tarefa.delete(0, tk.END)  #para limpar a caixa de texto automaticamnete

#criando o sql para adicionar as tarefas
       #criando a ocnexao
      conexao_adiciona = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")

      #criando o cursor
      cursor_adiciona = conexao_adiciona.cursor()

      #informações
      sql_inserir = """
                        INSERT INTO tarefa (descricao_tarefa)
                        VALUES (?)
                    """
      #executar a tabela
      cursor_adiciona.execute(sql_inserir,[self.texto])

      conexao_adiciona.commit()
      cursor_adiciona.close()
      conexao_adiciona.close()

#def para excluir a tarefa selecionada
    def excluir(self):
      self.selecionado = self.lista.curselection()  # pega o índice do item selecionado
      if self.selecionado:  # se algum item estiver selecionado
        self.lista.delete(self.selecionado[0])

      else:
        tk.messagebox.showerror(message="Selecione o item que quer excluir")

        conexao_delete = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")

        cursor_delete = conexao_delete.cursor()

        sql_delete_tabela = """
                            
                            """
        cursor_delete.execute(sql_delete_tabela)
        
        


      

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
