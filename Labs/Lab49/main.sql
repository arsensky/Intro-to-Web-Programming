-- Lab 1: Creating and Inserting Data into a Table
CREATE TABLE users (
    user_id           SERIAL PRIMARY KEY,
    name              TEXT        NOT NULL,
    email             TEXT UNIQUE NOT NULL,
    age               INTEGER,
    registration_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO users (name, email, age) VALUES
('Alice Johnson', 'alice@example.com', 28),
('Bob Smith', 'bob@example.com', 32),
('Charlie Brown', 'charlie@example.com', 25);

SELECT * FROM users;

-- Lab 2: Updating Records in a Table
UPDATE users
SET age = 29
WHERE name = 'Alice Johnson';

UPDATE users
SET email = 'charlie.brown@example.com'
WHERE name = 'Charlie Brown';

SELECT * FROM users;

-- Lab 3: Deleting Records from a Table
DELETE FROM users
WHERE email = 'bob@example.com';

DELETE FROM users
WHERE age > 30;

SELECT * FROM users;

-- Lab 4: Inserting, Updating, and Deleting in a Products Table
CREATE TABLE products (
    product_id     SERIAL PRIMARY KEY,
    product_name   TEXT           NOT NULL,
    price          NUMERIC(10, 2) NOT NULL,
    stock_quantity INTEGER        NOT NULL,
    discontinued   BOOLEAN DEFAULT FALSE
);

INSERT INTO products (product_name, price, stock_quantity) VALUES
('Laptop', 999.99, 10),
('Smartphone', 599.99, 20),
('Headphones', 199.99, 15);

UPDATE products
SET price = 1099.99
WHERE product_name = 'Laptop';

UPDATE products
SET discontinued = TRUE
WHERE product_name = 'Headphones';

DELETE FROM products
WHERE discontinued = TRUE;

SELECT * FROM products;

-- Lab 5: Practicing Data Manipulation with Transactions
BEGIN;

INSERT INTO users (name, email, age) VALUES
('David Green', 'david@example.com', 40);

UPDATE users
SET age = 35
WHERE name = 'Alice Johnson';

DELETE FROM users
WHERE name = 'Charlie Brown';

ROLLBACK;

SELECT * FROM users;