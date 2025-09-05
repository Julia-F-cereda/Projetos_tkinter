import ttkbootstrap as ttk
from classe_bot_gemini import Boot_gemini
class Janela_chat():
    def __init__(self):

        #criação de janela, ttk pq é o apelido do ttkbootstrap
        self.janela = ttk.Window( themename= "solar",
                                title="Ms. Sokie",
                                  )
        self.janela.iconbitmap("03_bot_gemini/coracao.ico")
        self.janela.geometry("800x600")

        #titulo
        self.label_titulo = ttk.Label(self.janela,
                                text="Bem vindo ao Mr. sokie",
                                foreground="pink",
                                style="dangerj",
                                font=('Times-New-Roman',20))
                                
                                
        self.label_titulo.pack(pady=20)

        #faça sua pergunta
        self.label_titulo2 = ttk.Label(self.janela,
                                       text="Insira a sua pergunta na caixa abaixo",
                                        foreground="purple",
                                       font=('Times-New-Roman',20))
                                  
        self.label_titulo2.pack(pady=20)

        #caixa de texto
        self.fazer_pergunta = ttk.Entry(self.janela)
        self.fazer_pergunta.pack(pady=20)


        #diga bom dia ao pressionar o botao

        #botao p responder a pergunta
        self.button_perguntar = ttk.Button(self.janela,
                                text="Perguntar",

                                                )
        self.button_perguntar.pack(pady=20)

        self.Label_reposta = ttk.Label(self.janela,
                                       text="RESPOSTA",
                                       )
        self.Label_reposta.pack(pady=20)

    def responder(self):
        pergunta = self.fazer_pergunta.get()
        robo = Boot_gemini

    



    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    chat = Janela_chat()
    chat.janela.mainloop() 
          