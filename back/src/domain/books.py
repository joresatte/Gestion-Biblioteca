import sqlite3


class Book:
    def __init__(self, id, title, author, publisher, ean):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.ean = ean

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "ean": self.ean,
        }


class BookRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE if not exists books (
                "id" TEXT,
                "title" TEXT,
                "author" TEXT,
                "publisher" TEXT,
                "ean" INTEGER, PRIMARY KEY("id")
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_books(self):
        sql = """select * from books"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            book = Book(**item)
            result.append(book)

        return result

    def get_book_by_id(self, id):
        sql = """SELECT * FROM books WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        book = Book(**data)
        return book

    def delete(self, id):
        sql = """DELETE FROM books WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        conn.commit()

    def save(self, book):
        sql = """insert into books (id, title, author, publisher, ean) values (
           :id, :title, :author, :publisher,:ean
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, book.to_dict())
        conn.commit()

    def edit(self, book):
        sql = """UPDATE books SET title= ?, author = ?, publisher= ?, ean= ? WHERE id = ?"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, (book.title, book.author,
                       book.publisher, book.ean, book.id))
        conn.commit()
