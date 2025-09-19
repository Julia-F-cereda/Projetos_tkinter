import ttkbootstrap as ttk
import tkinter.messagebox
class Menu_login():
   def __init__(self):
      self.menu_login = ttk.Window(themename="superhero",
                                  title="Tela de Login")
      
      self.menu_login.geometry("600x800")

      #Label titulo de cima login
      self.Label_titulo = ttk.Label(self.menu_login,
                                    text="Login",
                                    foreground="pink",
                                    font=("Times New Roman",40))
      self.Label_titulo.pack(pady=10)

      #Label para o nome da caixa usuario
      self.label_usuario = ttk.Label(self.menu_login,
                                     text="Usuário",
                                     font=("Times New Roman",15))
      self.label_usuario.pack()

      #Entry caixa para por o login
      self.entry_usuario = ttk.Entry(self.menu_login,
                                   text="Usuário")
      self.entry_usuario.pack(pady=10)

      #label para o nome senha
      self.label_senha = ttk.Label(self.menu_login,
                                   text="Senha",
                                   font=("Times New Roman",15))
      self.label_senha.pack()

      #entry para por a caixa p senha
      self.entry_senha = ttk.Entry(self.menu_login,
                                   text="Senha",
                                   show="*") #para mnao mosrrar a senha
      self.entry_senha.pack()

      
      #botão para logar
      frame_botao = ttk.Frame()
      frame_botao.pack()

      ttk.Button(frame_botao, text="LOGAR",width=30, command=self.conferir).pack(side="left", padx=20, pady=(20,0))
      ttk.Button(frame_botao, text="SAIR",width=30, command=self.menu_login.destroy).pack(side="right",padx=20, pady=(20,0))

          #loguin erradi


      
   def conferir(self):
      usuario = (self.entry_usuario.get())
      senha = (self.entry_senha.get())

#esse message box aparece um acaixinha de texto
      if usuario == "Godofredo" and senha == "amogirassol":
         tkinter.messagebox.showwarning(message="Login correto")
      else:
         tkinter.messagebox.showerror(message="Login e senha Incorreto")



      

      


                             






      






   def run(self):
      self.menu_login.mainloop()



      
      
      
      
      