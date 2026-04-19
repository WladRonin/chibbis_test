-- Считаем все таблички STG-слоем, поэтому загружаем почти "as is"
-- Сначала удаляем таблички, на случай если нам понадобится поменять их структуру

DROP TABLE IF EXISTS stg_users;
CREATE TABLE stg_users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    website TEXT,
    --
    address_street TEXT,
    address_suite TEXT,
    address_city TEXT,
    address_zipcode TEXT,
    address_geo_lat REAL,
    address_geo_lng REAL,
    --
    company_name TEXT,
    company_catchPhrase TEXT,
    company_bs TEXT,
    --
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.typicode.com/users'
);

DROP TABLE IF EXISTS stg_posts;
CREATE TABLE stg_posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT,
    --
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.typicode.com/posts',
    FOREIGN KEY (userId) REFERENCES stg_users (id)
);

DROP TABLE IF EXISTS stg_comments;
CREATE TABLE stg_comments (
    id INTEGER PRIMARY KEY,
    postId INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL, -- Интересная система, что мы привязываемся не к юзеру, а к email
                         -- Возможно дело в том, что комментировать можно без логина, но все равно странно
    body TEXT,
    --
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.typicode.com/comments',
    FOREIGN KEY (postId) REFERENCES stg_posts (id)
);