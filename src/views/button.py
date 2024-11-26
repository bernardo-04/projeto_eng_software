import customtkinter as ctk
from PIL import Image


class Button(ctk.CTkButton):
  def __init__(self, master, imagePath, buttonText, imgSizeX=20, imgSizeY=20, btnWidth=80, status="notClicked", btnHeight=50, **kwargs):
    super().__init__(master, width=50, corner_radius=0, fg_color="transparent", **kwargs)
    self.pack(padx=15, pady=10)

    self.buttonIcon = ctk.CTkImage(
        light_image=Image.open(imagePath), size=(imgSizeX, imgSizeY))
    self.coloredButtonIcon = ctk.CTkImage(
        light_image=Image.open(f"{imagePath[:-4]}_blue.png"), size=(imgSizeX, imgSizeY))
    self.configure(
        text=buttonText,
        width=btnWidth,
        height=btnHeight,
        image=self.buttonIcon,
        compound="top",
        corner_radius=10,
        border_width=2.5,
        fg_color="transparent",
        text_color="gray",
        font=("Poppins", 12),
        border_color="white"
    )

    self.bind("<Enter>", self.hover_in)
    self.bind("<Leave>", self.hover_out)
    self.bind("<ButtonPress-1>", self.on_click)
    self.bind("<ButtonRelease-1>", self.on_release)

  def hover_in(self, e):
    self.configure(
        border_color="#1a80fc",
        text_color="#1a80fc",
        image=self.coloredButtonIcon
    )

  def hover_out(self, e):
    self.configure(
        border_color="white",
        text_color="gray",
        image=self.buttonIcon
    )

  def on_click(self, e):
    if self.status == "clicked":
      self.configure(
          border_color="#1a80fc",
          text_color="#1a80fc",
          image=self.coloredButtonIcon
      )
      self.status = "notClicked"

  def on_release(self, e):
    self.configure(border_color="white", image=self.buttonIcon)


1
