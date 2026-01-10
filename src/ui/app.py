import customtkinter as ctk
from ui.sidebar import Sidebar
from ui.views.dashboard import DashboardView
from ui.views.info import InfoView

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("BMW Cluster Tools")
        self.geometry("1000x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.sidebar = Sidebar(self, controller=self)
        self.sidebar.pack(side="left", fill="y")

        self.container = ctk.CTkFrame(self)
        self.container.pack(side="right", fill="both", expand=True)

        self.views = {
            "dashboard": DashboardView(self.container),
            "info": InfoView(self.container),
        }

        self.current_view = None
        self.show_view("dashboard")

    def show_view(self, name: str):
        if self.current_view:
            self.current_view.pack_forget()

        view = self.views[name]
        view.pack(fill="both", expand=True)
        self.current_view = view
