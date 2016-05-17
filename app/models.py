
class BookModel:

    books = {
        "4873117569": {"name": "Effective Python ―Pythonプログラムを改良する59項目", "author": "Brett Slatkin"},
        "4873117380": {"name": "入門 Python 3", "author": "Bill Lubanovic"},
        "4873117402": {"name": "ハイパフォーマンスPython", "author": "Micha Gorelick"},
        "4873117399": {"name": "実践 Python 3", "author": "Mark Summerfield"}
    }

    def find(self, isbn):
        return self.books.get(isbn, None) if isbn else None

    def save(self, book):
        pass
