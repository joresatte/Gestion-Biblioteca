from urllib import response
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.loans import LoanRepository, Loan


def test_delete_method_should_delete_loaned_book():
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

    response_delete = client.delete("/api/loans/loan-1")
    assert response_delete.status_code == 200

    repository_response = loans_repository.get_loans()
    response_list = []
    for item in repository_response:
        response_list.append(item.to_dict())

    assert response_list == [
        {
            "loan_id": "loan-2",
            "book_id": "book-2",
            "user_id": "user_2"
        }
    ]
