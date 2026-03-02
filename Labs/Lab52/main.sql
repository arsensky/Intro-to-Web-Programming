CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )

INSERT INTO customers (name, email) VALUES
('Alice', 'alice@email.com'),
('Bob', 'bob@email.com'),
('John', 'john@email.com')
ON CONFLICT DO NOTHING;

INSERT INTO orders (customer_id, total_amount) VALUES
(1, 250.00),
(2, 120.00),
(1, 80.00),
(NULL, 300.00)
ON CONFLICT DO NOTHING;

-- INNER JOIN: Joining Customers and Orders Tables
SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;

-- LEFT JOIN: Retrieving All Customers and Their Orders (Even Those Without Orders)
SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;

-- RIGHT JOIN: Retrieving All Orders and Their Customers (Even Those Without Registered Customers)
SELECT orders.order_id, orders.total_amount, customers.name
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;

-- FULL JOIN: Retrieving All Customers and All Orders (Even If No Match Exists)
SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
FULL JOIN orders
ON customers.customer_id = orders.customer_id;