CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255)NOT NULL
);

INSERT INTO users (username, email) VALUES
    ('anjali', 'anjali@gmail.com');


SELECT * FROM users