from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.books import BookRepository, Book


def test_should_return_one_book_by_id():
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

    response = client.get("/api/books/book-1")
    assert response.json == {
        "id": "book-1",
        "title": "test title",
        "author": "test author",
        "publisher": "test publisher",
        "ean": 1111,
    }
