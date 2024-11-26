import customtkinter as ctk
from PIL import Image
from views.button import Button


class SideBar(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, width=50, corner_radius=0, fg_color="transparent", **kwargs)
    self.pack(side="left", fill="y")

    # SideBar Buttons
    self.homeButton = Button(self, "src/views/icons/home.png", "Home")
    self.homeButton.pack()

    self.customersButton = Button(
        self, "src/views/icons/customer.png", "Clientes")
    self.customersButton.pack()

    self.productsButton = Button(
        self, "src/views/icons/products.png", "Produtos")
    self.productsButton.pack()

    self.salesButton = Button(
        self, "src/views/icons/price-tag.png", "Vendas", imgSizeX=24, imgSizeY=24)
    self.salesButton.pack()
