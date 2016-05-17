from app import models


class TestBookModel:
    """
    BookModelTest はだめ
    TestBookModel じゃないと nose が検知してくんない (Class は "Test****" というのが標準ルールの模様)
    """

    def test_find(self):
        book = models.BookModel().find("4873117569")
        assert book
        assert book.get("name") == "Effective Python ―Pythonプログラムを改良する59項目"

    def test_save(self):
        pass  # 何もしねー
