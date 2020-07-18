class Button:
    def __init__(self, text):
        pass

class Toolbar:
    pass

class Window:
    def __init__(self, title):
        pass


DEFAULT_STYLE = {
    "button": Button,
    "toolbar": Toolbar,
    "window": Window
}

class Application:

    def __init__(self, theme):
        self.theme = theme

    def start(self):
        main_window = self.theme["window"](title="My Awesome app!")
        buttons = [self.theme["button"](text) for text in ("OK", "Cancel")]
        toolbar = self.theme["toolbar"]()
        # Wyświetl jakoś utworzone elementy.


if __name__ == '__main__':
    app = Application(DEFAULT_STYLE)
    app.start()

