
from src.lib.utils import temp_file, object_to_json

from src.webserver import create_app
from src.domain.loans import LoanRepository, Loan


def test_should_create_loans():
    loans_repository = LoanRepository(temp_file())
    app = create_app(repositories={"loans": loans_repository})
    client = app.test_client()

    loans_repository.save(
        Loan(
            loan_id="loan-1",
            book_id="book-1",
            user_id="user_1"
        )
    )

    loans_repository.save(
        Loan(
            loan_id="loan-2",
            book_id="book-2",
            user_id="user_2"
        )
    )

    response = client.get("/api/loans")

    assert response.json == [
        {
            "loan_id": "loan-1",
            "book_id": "book-1",
            "user_id": "user_1"
        },
        {
            "loan_id": "loan-2",
            "book_id": "book-2",
            "user_id": "user_2"
        }
    ]
