class TextDocument:
    pass

class ModernDocuemnt:
    pass

class Resume:
    pass

class ModernResume:
    pass


class DocumentCreator:

    def __init__(self, new_text_document, new_resume):
        self.new_text_document = new_text_document
        self.new_resume = new_resume

    def create_text_document(self):
        document = self.new_text_document()
        # Zrób coś jeszcze

    def create_resume(self):
        document = self.new_resume()


if __name__ == '__main__':
    creator_1 = DocumentCreator(
        new_text_document=TextDocument,
        new_resume=Resume
    )
