import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, width=200)
        self.controller = controller

        self.pack_propagate(False)

        title = ctk.CTkLabel(self, text="BMW Tools", font=("Arial", 20))
        title.pack(pady=20)

        ctk.CTkButton(self, text="Dashboard",
                      command=lambda: controller.show_view("dashboard")).pack(pady=10)

        ctk.CTkButton(self, text="Info",
                      command=lambda: controller.show_view("info")).pack(pady=10)
