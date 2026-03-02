-- 1. Creating a Users Table
CREATE TABLE users (
    id         SERIAL PRIMARY KEY,
    full_name  TEXT                NOT NULL,
    email      VARCHAR(100) UNIQUE NOT NULL,
    birth_date DATE                NOT NULL,
    is_active  BOOLEAN DEFAULT TRUE
);

--- Verify the table structure
SELECT * FROM users;

-- 2. Creating a Products Table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name       TEXT           NOT NULL,
    price      DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--- Verify
SELECT * FROM products;

-- 3. Dropping a Table
DROP TABLE IF EXISTS products;

--- Verify by trying to select from the table (should give an error)
SELECT * FROM products;

-- 4. Altering a Table – Adding a Column
ALTER TABLE users ADD COLUMN phone_number VARCHAR(20);

--- Verify
SELECT phone_number FROM users;

-- 5. Altering a Table – Removing a Column
ALTER TABLE users DROP COLUMN phone_number;

--- Verify (should give an error)
SELECT phone_number FROM users;

-- 6. Altering a Table – Renaming a Column
ALTER TABLE users RENAME COLUMN full_name TO name;

--- Verify
SELECT name FROM users;

-- 7. Altering a Table – Changing a Column Data Type
ALTER TABLE products ALTER COLUMN price TYPE INTEGER;

--- Verify
SELECT price FROM products;