import customtkinter as ctk

class KLineView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(self, text="K-Line Tools", font=("Arial", 24))
        label.pack(pady=20)

        ctk.CTkLabel(self, text="Zde budou funkce pro K-Line diagnostiku.").pack(pady=10)
