import customtkinter as ctk
import serial.tools.list_ports

class DashboardView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 24))
        title.pack(pady=20)

        # --- COM PORT SELECT ---
        ports_label = ctk.CTkLabel(self, text="COM Port:")
        ports_label.pack()

        self.port_var = ctk.StringVar()
        self.port_menu = ctk.CTkOptionMenu(self, variable=self.port_var,
                                           values=self.get_ports())
        self.port_menu.pack(pady=5)

        # --- CONNECT / DISCONNECT ---
        self.connect_btn = ctk.CTkButton(self, text="Připojit", command=self.connect)
        self.connect_btn.pack(pady=10)

        self.disconnect_btn = ctk.CTkButton(self, text="Odpojit", command=self.disconnect)
        self.disconnect_btn.pack(pady=5)

        # --- BATTERY / IGNITION ---
        ctk.CTkLabel(self, text="Simulace napájení:").pack(pady=10)

        self.batt_btn = ctk.CTkButton(self, text="Battery ON", command=self.battery_on)
        self.batt_btn.pack(pady=5)

        self.ign_btn = ctk.CTkButton(self, text="Ignition ON", command=self.ignition_on)
        self.ign_btn.pack(pady=5)

        # --- ADVANCED SETTINGS ---
        ctk.CTkLabel(self, text="Advanced nastavení:").pack(pady=15)

        self.baud_var = ctk.StringVar(value="9600")
        ctk.CTkLabel(self, text="Baudrate:").pack()
        ctk.CTkEntry(self, textvariable=self.baud_var).pack(pady=5)

        self.databits_var = ctk.StringVar(value="8")
        ctk.CTkLabel(self, text="Data bits:").pack()
        ctk.CTkEntry(self, textvariable=self.databits_var).pack(pady=5)

        self.parity_var = ctk.StringVar(value="N")
        ctk.CTkLabel(self, text="Parity (N/E/O):").pack()
        ctk.CTkEntry(self, textvariable=self.parity_var).pack(pady=5)

        self.stopbits_var = ctk.StringVar(value="1")
        ctk.CTkLabel(self, text="Stop bits:").pack()
        ctk.CTkEntry(self, textvariable=self.stopbits_var).pack(pady=5)

    def get_ports(self):
        return [p.device for p in serial.tools.list_ports.comports()]

    # --- Placeholder funkce ---
    def connect(self):
        print("Připojit (zatím mock)")

    def disconnect(self):
        print("Odpojit (zatím mock)")

    def battery_on(self):
        print("Battery ON (zatím mock)")

    def ignition_on(self):
        print("Ignition ON (zatím mock)")
