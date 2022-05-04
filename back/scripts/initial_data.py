import sys
sys.path.insert(0, "")


def data_organizer():
    from src.domain.users import UserRepository, User
    from src.domain.info import InfoRepository, Info
    import sqlite3
    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info("library-app"))

    con = sqlite3.connect(database_path)
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(
        """CREATE TABLE books 
    ("id" TEXT,
    "title" TEXT, 
    "author" TEXT, 
    "publisher" TEXT, 
    "ean" INTEGER, PRIMARY KEY("id") )"""
    )

    cur.execute(
        """INSERT INTO books 
    VALUES
    ('book-1','Escenografía y maquillaje', 'Martí, Mònica', 'Parramon', '978843342202'),
    ('book-2','Titeres y mimo', 'Martí, Mònica', 'Parramon',    '978843342208'),
    ('book-3','Carrie',    'King, Stephen',    'Debolsillo',    '978843342206'),
    ('book-4','Armas, gérmenes y acero',    'Diamond, Jared',    'Debolsillo',    '978843342204'),
    ('book-5','Egipto',    'Bargallo, Eva',    'Parramon',    '978843342200');"""
    )

    cur.execute(
        """CREATE TABLE users
    ("user_id" TEXT,
    "user" TEXT,
    "is_librarian" INTGER, 
    PRIMARY KEY("user_id") )"""
    )

    cur.execute(
        """INSERT INTO users 
    VALUES
    ('user_1','Paco Fernandez', True),
    ('user_2','Bob Deeb', False),
    ('user_3','Anna',False);"""
    )
    cur.execute(
        """
                CREATE TABLE if not exists loans (
                    "loan_id" TEXT,
                    "book_id" TEXT,
                    "user_id" TEXT,
                    PRIMARY KEY("loan_id")
                )
            """
    )

    con.commit()
    cur.close()


data_organizer()
