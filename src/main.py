from ui.app import App
from logic.controller import Controller

app = App()

def main():
    controller = Controller(app)
    app.controller = controller
    app.mainloop()

if __name__ == "__main__":
    main()
