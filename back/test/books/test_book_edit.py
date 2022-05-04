from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.books import BookRepository, Book


def test_method_should_edit_one_book():
    books_repository = BookRepository(temp_file())
    app = create_app(repositories={"books": books_repository})
    client = app.test_client()

    books_repository.save(
        Book(
            id="book-1",
            title="test title",
            author="test author",
            publisher="test publisher",
            ean=1111,
        )
    )
    book_data = Book("book-1", "edited title",
                     "edited author", "edited publisher", 2222)
    books_repository.edit(book_data)
    response_get = client.get("/api/books/book-1")

    assert response_get.json == {
        "id": "book-1",
        "title": "edited title",
        "author": "edited author",
        "publisher": "edited publisher",
        "ean": 2222,
    }


def test_server_should_edit_one_book():
    books_repository = BookRepository(temp_file())
    app = create_app(repositories={"books": books_repository})
    client = app.test_client()

    books_repository.save(
        Book(
            id="book-1",
            title="test title",
            author="test author",
            publisher="test publisher",
            ean=1111,
        )
    )
    book_data = {"id": "book-1", "title": "edited title",
                 "author": "edited author", "publisher": "edited publisher", "ean": 2222}

    response = client.post("/api/books/book-1", json=book_data)
    assert response.status_code == 200
    response_get = client.get("/api/books/book-1")

    assert response_get.json == {
        "id": "book-1",
        "title": "edited title",
        "author": "edited author",
        "publisher": "edited publisher",
        "ean": 2222,
    }
