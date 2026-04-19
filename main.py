import argparse
import logging
from pathlib import Path
from pydantic import ValidationError
from src.database import Database
from src.api_client import ServiceClient
from src.schemas import Users, Posts, Comments

DATABASE_PATH = "data/my_database.db"

parser = argparse.ArgumentParser(description="Тестовая интеграция")
parser.add_argument("-r", "--reset", action="store_true", 
    help="Принудительная инициализация схемы БД из scripts/schema.sql")
args = parser.parse_args()

db_exists_flag = Path(DATABASE_PATH).exists() and not args.reset

logging.info("Инициализация базы данных...")
db_manager = Database(DATABASE_PATH, db_exists_flag)

logging.info("Загрузка данных из источника...")
with ServiceClient() as sc:
    raw_users = sc.get_users()
    raw_posts = sc.get_posts()
    raw_comments = sc.get_comments()

logging.info("Валидация данных...")
users = [Users.model_validate(u) for u in raw_users]
posts = [Posts.model_validate(u) for u in raw_posts]
comments = [Comments.model_validate(u) for u in raw_comments]

logging.info("Загрузка данных в БД...")
try:
    db_manager.upload_table("stg_users", users)
    db_manager.upload_table("stg_posts", posts)
    db_manager.upload_table("stg_comments", comments)
except ValidationError as err:
    logging.error(f"Ошибка при валидации данных: {err}")
    raise

logging.info("Загрузка завершена!")
