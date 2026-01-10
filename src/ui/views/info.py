import customtkinter as ctk

class InfoView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Informace o budících", font=("Arial", 24))
        title.pack(pady=20)

        self.info_box = ctk.CTkTextbox(self, width=600, height=300)
        self.info_box.pack(pady=10)

        self.info_box.insert("end", "Zde se zobrazí informace o IKE.\n")
        self.info_box.insert("end", "VIN, HW/SW verze, indexy, coding...\n")
