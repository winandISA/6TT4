# =========================
# DB Singleton
# =========================
import sqlite3


class DbConnection:
    _instance = None

    def __new__(cls, db_path="db/app.db"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(db_path)
        return cls._instance

    def _init(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def execute(self, sql: str, params: tuple = ()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        return cur

    def close(self):
        self.conn.close()
