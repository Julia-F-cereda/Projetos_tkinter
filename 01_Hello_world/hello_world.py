import tkinter as tk

#criando janela
janela = tk.Tk()

#definindo titulo
janela.title("Hello World")

#pintar a tela
janela.configure(bg="pink")

#colocar icone
janela.iconbitmap("01_Hello_world/snowflake.ico")

#tamanho
janela.geometry("800x400+100+200")

#
janela.resizable(False,False)

#criando bem vindo
label_titulo = tk.Label(janela,
                        text="Bem vindo!",
                        bg="purple",
                        font="arial",
                        foreground="pink")
label_titulo.pack()

#criando texto diga seu nome
label_text = tk.Label(janela, 
                      text="Digite seu nome:")
label_text.pack()

#caixa de texto
entry_nome = tk.Entry(janela)
entry_nome.pack()

#botao pro bom dia
button_bomdia = tk.Button(janela,
                          text="Diga bom dia")
button_bomdia.pack()

#dizendo bom dia
label_bomdia = tk.Label(janela,
                        text=f"Bom dia,")
label_bomdia.pack()


#loop pra manter janela aberta
janela.mainloop()


