-- Считаем все таблички STG-слоем, поэтому загружаем почти "as is"

CREATE TABLE IF NOT EXISTS stg_companies (
    tk INTEGER PRIMARY KEY, -- добавил технический ключ
    name TEXT,
    catchPhrase TEXT,
    bs TEXT,
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.com'
);

CREATE TABLE IF NOT EXISTS stg_addresses (
    tk INTEGER PRIMARY KEY, -- добавил технический ключ
    street TEXT,
    suite TEXT,
    city TEXT,
    zipcode TEXT,
    geo_lat REAL,
    geo_lng REAL,
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.com'
);

CREATE TABLE IF NOT EXISTS stg_users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    website TEXT,
    adress_tk INTEGER DEFAULT -2,
    company_tk INTEGER DEFAULT -2,
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.com',
    FOREIGN KEY (adress_tk) REFERENCES stg_addresses (tk),
    FOREIGN KEY (company_tk) REFERENCES stg_companies (tk)
);

CREATE TABLE IF NOT EXISTS stg_posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT,
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.com',
    FOREIGN KEY (userId) REFERENCES stg_users (id)
);

CREATE TABLE IF NOT EXISTS stg_comments (
    id INTEGER PRIMARY KEY,
    postId INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL, -- Интересная система, что мы привязываемся не к юзеру, а к email
                         -- Возможно дело в том, что комментировать можно без логина, но все равно странно
    body TEXT,
    extracted_dttm DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_system TEXT DEFAULT 'jsonplaceholder.com',
    FOREIGN KEY (postId) REFERENCES stg_posts (id)
);