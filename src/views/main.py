import sys
from pathlib import Path
import customtkinter as ctk

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from views.header import Header
from views.sidebar import SideBar

ctk.set_appearance_mode("light")


class Main(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Projeto ESW")
    self.geometry("800x800")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.configure(fg_color="white")

    self.header = Header(self)
    self.header.pack()

app = Main()
app.mainloop()
