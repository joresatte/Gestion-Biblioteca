from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.books import BookRepository, Book


def test_delete_method_should_delete_one_book():
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
    books_repository.save(
        Book(
            id="book-2",
            title="test title",
            author="test author",
            publisher="test publisher",
            ean=2222,
        )
    )

    books_repository.delete("book-1")

    response_get = client.get("/api/books")

    assert response_get.json == [
        {
            "id": "book-2",
            "title": "test title",
            "author": "test author",
            "publisher": "test publisher",
            "ean": 2222,
        }
    ]


def test_server_should_delete_one_book():
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
    books_repository.save(
        Book(
            id="book-2",
            title="test title",
            author="test author",
            publisher="test publisher",
            ean=2222,
        )
    )

    response = client.delete("/api/books/book-1")
    assert response.status_code == 200

    response_get = client.get("/api/books")

    assert response_get.json == [
        {
            "id": "book-2",
            "title": "test title",
            "author": "test author",
            "publisher": "test publisher",
            "ean": 2222,
        }
    ]
