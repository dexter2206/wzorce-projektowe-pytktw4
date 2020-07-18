class TextDocument:
    pass

class ModernDocuemnt:
    pass

class Resume:
    pass

class ModernResume:
    pass


class DefaultTheme:

    def new_text_document(self):
        print("Creating default text document.")
        return TextDocument()

    def new_resume(self):
        return Resume()

class ModernTheme:

    def new_text_document(self):
        print("Creating modern text document.")
        return ModernDocuemnt()

    def new_resume(self):
        return ModernResume()

class DocumentCreator:

    def __init__(self, theme):
        self.theme = theme

    def create_text_document(self):
        document = self.theme.new_text_document()
        # Zrób coś jeszcze

    def create_resume(self):
        document = self.theme.new_resume()
        # Zrób coś jeszcze


if __name__ == '__main__':
    theme_1 = DefaultTheme()
    theme_2 = ModernTheme()

    creator_1 = DocumentCreator(theme_1)
    creator_2 = DocumentCreator(theme_2)

    creator_1.create_text_document()
    creator_2.create_text_document()

