import ttkbootstrap as ttk
class main():
    def __init__(self):

        self.main = ttk.Window(themename="solar",
                               title="Calculador de IMC"
                               )

        self.main.geometry("600x800")

        #titulo cima
        self.Label_titulo = ttk.Label(self.main,
                                      text=""
                                      )



