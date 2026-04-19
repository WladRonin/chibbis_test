import logging
import sqlite3
from pydantic import validate_call
from src.schemas import Users, Posts, Comments

class Database:
    def __init__(self, db_path: str, db_exists: bool = True):
        self.db_path = db_path
        if not db_exists:
            try:
                with self._get_connection() as conn:
                    with open("scripts/schema.sql", "r") as f:
                        conn.executescript(f.read())
                    logging.info("Схема базы данных успешно инициализирована.")
            except Exception as e:
                logging.error(f"Ошибка при инициализации БД: {e}")
                raise
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables_info = cur.fetchall()
            self.tables_white_list = [table[0] for table in tables_info]


    def _get_connection(self):
        return sqlite3.connect(self.db_path)


    @validate_call
    def upload_table(self, table_name: str, data: list[Users | Posts | Comments]):
        try:
            if table_name not in self.tables_white_list:
                raise ValueError("Таблица не принадлежит этой БД")
            # Сборка кастомного sql-запроса должна быть достаточно безопасна в этом случае:
            # Имя таблицы проверяется по белому списку
            # Имена атрибутов проверяются по модели за счет @validate_call
            # Значения атрибутов заменяются плейсхолдерами "?"
            attr_list = list(data[0].model_dump())
            custom_insert_sql = f"INSERT INTO {table_name} ("
            custom_insert_sql += ", ".join(attr_list) + ")"
            custom_insert_sql += " VALUES (" + ", ".join(["?"]*len(attr_list)) + ")"
            with self._get_connection() as conn:
                cur = conn.cursor()
                cur.execute(f"DELETE FROM {table_name}")
                data_values_list = [tuple(item.model_dump().values()) for item in data]
                cur.executemany(custom_insert_sql, data_values_list)
                conn.commit()
                logging.info(f"Успешно загружено {len(data)} записей.")
        except ValueError as err:
            logging.error(f"Ошибка при вставке данных: {err}")
            raise
        except Exception as err:
            logging.error(f"Ошибка при вставке данных: {err}")
            raise