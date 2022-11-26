DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS variable;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE variable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    variable_text TEXT NOT NULL,
    variable_integer INTEGER NOT NULL,
    variable_float FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);