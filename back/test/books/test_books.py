from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.books import BookRepository, Book


def test_should_return_books_in_database():
    books_repository = BookRepository(temp_file())
    app = create_app(repositories={"books": books_repository})
    client = app.test_client()

    books_repository.save(
        Book(
            id="id",
            title="test title",
            author="test author",
            publisher="test publisher",
            ean=1111,
        )
    )

    response = client.get("/api/books")
    assert response.json == [
        {
            "id": "id",
            "title": "test title",
            "author": "test author",
            "publisher": "test publisher",
            "ean": 1111,
        },
    ]
