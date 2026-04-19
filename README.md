# chibbis_test
My test case for chibbis vacancy

ETL-процесс для загрузки данных из JSONPlaceholder в локальную базу данных SQLite. 

## Функционал
Модуль запускается с помощью python main.py
- Создает БД sqlite3 data/my_database.db, если отсутствует
- Запускает scripts/schema.sql для создания таблиц:
	- stg_users
	- stg_posts
	- stg_comments
- Загружает соответствующие данные из источника jsonplaceholder.typicode.com
	- Данные проверяются pydantic на соответствие scripts/schemas.py
	- Данные обновляются в целевых таблицах полной перегрузкой
	- Дополняются атрибутами extracted_dttm и source_system

Опция "-r" или "--reset" позволяет пересоздать структуру таблиц, заново вызывая scripts/schema.sql

## Требования и установка
0. Модуль создавался в python 3.14.4
	- Предположительно, должен работать с python >= 3.8
1. Клонируйте репозиторий.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
