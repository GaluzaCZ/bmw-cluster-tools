import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("BMW Tools")
        self.geometry("600x400")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Hlavní rám
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Nadpis
        self.label = ctk.CTkLabel(self.frame, text="BMW Cluster Tools", font=("Arial", 24))
        self.label.pack(pady=10)

        # Tlačítko
        self.button = ctk.CTkButton(
            self.frame,
            text="Test komunikace"
        )
        self.button.pack(pady=10)

        # Výstupní text
        self.output = ctk.CTkTextbox(self.frame, height=200)
        self.output.pack(pady=10, fill="both", expand=True)

    def log(self, text: str):
        self.output.insert("end", text + "\n")
        self.output.see("end")
