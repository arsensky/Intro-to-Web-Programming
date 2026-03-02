--- COUNT()
-- Counting all rows in a table (COUNT(*)):
SELECT COUNT(*) FROM employees;

-- Counting rows where a specific condition is met (COUNT() with WHERE):
SELECT COUNT (*) FROM employees WHERE department = 'IT';

-- Counting non-NULL values in a specific column:
SELECT COUNT (salary) FROM employees;

-- Using COUNT with GROUP BY:
SELECT department, COUNT(*) FROM employees GROUP BY department;

-- Combining COUNT with HAVING (after GROUP BY):
SELECT department, COUNT (*)
FROM employees
GROUP BY department
HAVING COUNT (*) >= 3;

--- SUM()
-- Summing all values in a numeric column:
SELECT SUM(total_amount) FROM orders;

-- Summing values with a condition (WHERE):
SELECT SUM(total_amount) FROM orders WHERE order_rate BETWEEN '2023-01-01' AND '2023-12-31';

-- Summing values grouped by a specific column (GROUP BY):
SELECT customer_id, SUM(total_amount)
FROM orders
GROUP BY customer_id;

-- Using SUM() with HAVING to filter groups:
SELECT customer_id, SUM(total_amount)
FROM orders
GROUP BY customer_id
HAVING SUM(total_amount) > 500;

-- Summing multiple columns:
SELECT SUM(price) + SUM(tax) AS total_price_and_tax
FROM sales;

-- Summing with DISTINCT:
SELECT SUM(DISTINCT price) FROM products;

--- AVG()
-- Calculating the average of all values in a numeric column:
SELECT AVG(total_amount) FROM sales;

-- Calculating the average value with a condition (WHERE):
SELECT AVG(total_amount) FROM sales WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

-- Calculating the average value grouped by another column (GROUP BY):
SELECT customer_id, AVG(total_amount)
FROM sales
GROUP BY customer_id;

-- Using AVG() with HAVING to filter groups:
SELECT customer_id, AVG(total_amount)
FROM sales
GROUP BY customer_id
HAVING AVG(total_amount) > 100;

-- Calculating the average with multiple columns (e.g., multiple items per order):
SELECT AVG(quantity) FROM order_items;

-- Combining AVG() with DISTINCT:
SELECT AVG(DISTINCT price) FROM products;

--- MIN()
-- Finding the minimum value in a column
SELECT MIN(price) FROM products;

-- Finding the minimum value with a condition (WHERE):
SELECT MIN(order_date) FROM orders WHERE order_status = 'shipped';

-- Finding the minimum value grouped by another column (GROUP BY):
SELECT category, MIN(price) FROM products GROUP BY category;

-- Using MIN() with HAVING to filter groups:
SELECT category, MIN(price) FROM products GROUP BY category HAVING MIN(price) > 50;

-- Finding the earliest date in a column (for date data types):
SELECT MIN(join_date) FROM employees;

-- Finding the lowest quantity in inventory:
SELECT product_name, MIN(quantity_in_stock) FROM inventory;

--- MAX()
-- Finding the maximum value in a column:
SELECT MAX(salary) FROM employees;

-- Finding the maximum value with a condition (WHERE):
SELECT MAX(order_date) FROM orders WHERE order_status = 'shipped';

-- Finding the maximum value grouped by another column (GROUP BY):
SELECT category, MAX(price) FROM products GROUP BY category;

-- Using MAX() with HAVING to filter groups:
SELECT category, MAX(price) FROM products GROUP BY category HAVING MAX(price) > 100;

-- Finding the latest date in a column (for date data types):
SELECT MAX(join_date) FROM employees;

-- Finding the maximum quantity in stock:
SELECT product_name, MAX(quantity_in_stock) FROM inventory;

--- GROUP BY and HAVING
-- Using GROUP BY without HAVING
SELECT store_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id;

-- Using GROUP BY with HAVING
SELECT store_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id
HAVING SUM(amount) > 100000;

-- Using GROUP BY with Multiple Columns
SELECT store_id, product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id, product_id;

-- Using GROUP BY with COUNT()
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;

-- Using GROUP BY with AVG()
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;

-- Using GROUP BY with HAVING and a Conditional Aggregate Function
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
HAVING SUM(salary) > 500000;

-- Using GROUP BY with HAVING and COUNT()
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;