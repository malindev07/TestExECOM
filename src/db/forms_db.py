from dataclasses import dataclass
from typing import Mapping, Any

from pymongo import MongoClient
from pymongo.synchronous.database import Database


class DataBaseConnection:
    db = None
    host: str
    port: int
    db_name: str

    def __init__(self, host: str, port: int, db_name: str) -> None:
        self.host = host
        self.port = port
        self.db_name = db_name
        self.db = self.get_db()

    @staticmethod
    def get_client():
        return MongoClient("mongodb://localhost:27017/")
        # return MongoClient("mongodb://mongodb:27017/")

    def get_db(self):
        connection = self.get_client()
        db = connection[self.db_name]
        return db


# con = DataBaseConnection(host="localhost", port=27017, db_name="forms_db")
# # con = DataBaseConnection(host="mongo", port=27017, db_name="forms_db")
#
# DB = con.get_db()


@dataclass
class SaveData:
    topic: str = "forms_db"

    @classmethod
    def save_data_to_db(cls, database: Database[Mapping[str, Any]], data: dict):
        database[cls.topic].insert_one(data)
