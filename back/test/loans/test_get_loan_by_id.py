from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.loans import LoanRepository, Loan


def test_should_return_true_if_book_is_loaned():
    loans_repository = LoanRepository(temp_file())
    app = create_app(repositories={"loans": loans_repository})
    client = app.test_client()

    loans_repository.save(
        Loan(
            loan_id="loan_1",
            book_id="book_1",
            user_id="user_1"
        )
    )

    response = client.get("/api/loans/loan_1")
    assert response.status_code == 200
