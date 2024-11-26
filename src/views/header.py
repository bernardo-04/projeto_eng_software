import customtkinter as ctk
from PIL import Image

class Header(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, height=50, corner_radius=0, fg_color="transparent", **kwargs)
    self.pack(side="top", fill="x")

    # Header Title
    self.title = ctk.CTkLabel(
        self, text="Sistema PDV", font=("Poppins", 24, "bold"))
    self.title.pack(side="left", padx=15, pady=10)

    # Header Buttons
    self.reloadIcon = ctk.CTkImage(
        light_image=Image.open("src/views/icons/reload.png"), size=(16, 16))
    self.reloadProducts = ctk.CTkButton(
        self, text="", image=self.reloadIcon, anchor="center", width=35, height=35, fg_color="#edebeb", hover=False)
    self.reloadProducts.pack(side="right", padx=15)
