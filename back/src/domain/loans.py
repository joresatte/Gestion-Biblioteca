import sqlite3


class Loan:
    def __init__(self, loan_id, book_id, user_id):
        self.loan_id = loan_id
        self.book_id = book_id
        self.user_id = user_id

    def to_dict(self):
        return {

            "loan_id": self.loan_id,
            "book_id": self.book_id,
            "user_id": self.user_id,

        }


class LoanRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE if not exists loans (
                "loan_id" TEXT,
                "book_id" TEXT,
                "user_id" TEXT,
                PRIMARY KEY("loan_id")
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_loans(self):
        sql = """select * from loans"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            loan = Loan(**item)
            result.append(loan)

        return result

    def save(self, loan):
        sql = """insert into loans (loan_id, book_id, user_id) values (
           :loan_id, :book_id, :user_id
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, loan.to_dict())
        conn.commit()

    def delete(self, loan_id):
        sql = """DELETE FROM loans WHERE loan_id = :loan_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"loan_id": loan_id})

        conn.commit()

    def is_loaned(self, book_id):
        sql = """SELECT * FROM loans
        WHERE loans.book_id == :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": book_id})

        data = cursor.fetchall()
        if data == []:
            return True
        else:
            return False
