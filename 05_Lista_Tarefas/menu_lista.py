import ttkbootstrap as ttk
class Menu_lista:
    def __init__(self):

       self.menu_lista = ttk.Window(themename="superhero",
                                    title="")
       
       self.menu_lista.geometry("600x800")







    def run(self):
      self.menu_lista.mainloop()

if __name__ == "__main__":
    lista = Menu_lista()
    lista.run()
