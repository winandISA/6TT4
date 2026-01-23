import sqlite3
from abc import ABCMeta, ABC, abstractmethod

from tkinter_ex.classes.db.DbConnection import DbConnection


class DAO(ABC):
    def __init__(self):
        self.db = DbConnection()
        self.create_table()

    @abstractmethod
    def create_table(self):
        pass

# =========================
# DAO (accès DB)
# =========================
class UserDao(DAO):
    def __init__(self):
        super().__init__()

    def create_table(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS TUser(
            Id_User INTEGER PRIMARY KEY AUTOINCREMENT,
            Nom TEXT NOT NULL UNIQUE,
            Password TEXT NOT NULL
        );
        """)

    def add_user(self, nom: str, pwd: str) -> bool:
        try:
            self.db.execute(
                "INSERT INTO TUser(Nom, Password) VALUES (?, ?)",
                (nom, pwd)
            )
            return True
        except sqlite3.IntegrityError:
            # Nom déjà existant (UNIQUE)
            return False

    def user_exists(self, nom: str, pwd: str) -> bool:
        cur = self.db.execute(
            "SELECT 1 FROM TUser WHERE Nom = ? AND Password = ?",
            (nom, pwd)
        )
        return cur.fetchone() is not None

    def get_all_usernames(self) -> list[str]:
        cur = self.db.execute("SELECT Nom FROM TUser ORDER BY Nom")
        liste = []
        for row in cur.fetchall():
            liste.append(row["Nom"])
        return liste
