from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.books import BookRepository, Book


def test_server_should_save_one_book():
    books_repository = BookRepository(temp_file())
    app = create_app(repositories={"books": books_repository})
    client = app.test_client()

    book = {
        "id": "book-1",
        "title": "test title",
        "author": "test author",
        "publisher": "test publisher",
        "ean": 1111,
    }

    response = client.post("/api/books", json=book)

    assert response.status_code == 200
    response_get = client.get("/api/books/book-1")

    assert response_get.json == {
        "id": "book-1",
        "title": "test title",
        "author": "test author",
        "publisher": "test publisher",
        "ean": 1111
    }
