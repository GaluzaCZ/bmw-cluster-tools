class Controller:

    def __init__(self, app):
        self.app = app

    def test_connection(self):
        # Tady později přidáš diagnostiku, K-Line, K-Bus…
        self.app.log("Test komunikace OK (zatím jen mock).")
