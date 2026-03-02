CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    salary INTEGER,
    hire_date DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Alice', 'Smith', 'HR', 50000, '2020-06-15'),
('Bob', 'Johnson', 'IT', 70000, '2019-08-23'),
('Charlie', 'Williams', 'Finance', 65000, '2021-03-11'),
('David', 'Brown', 'IT', 72000, '2018-09-30'),
('Emma', 'Davis', 'HR', 48000, '2022-01-05');

SELECT * FROM employees;

SELECT first_name, salary FROM employees;

SELECT * FROM employees WHERE department = 'IT';

SELECT * FROM employees WHERE salary > 60000;

SELECT * FROM employees WHERE hire_date > '2020-01-01';

SELECT * FROM employees WHERE department IN ('HR', 'Finance');

SELECT * FROM employees WHERE first_name LIKE 'A%';

SELECT * FROM employees WHERE last_name LIKE '%son';

SELECT * FROM employees WHERE first_name LIKE '%e';

SELECT * FROM employees WHERE salary BETWEEN 50000 AND 70000;

SELECT * FROM employees WHERE hire_date BETWEEN '2019-01-01' AND '2021-12-31';

SELECT * FROM employees WHERE department IN ('IT', 'HR');

SELECT * FROM employees WHERE salary IN (48000, 65000, 72000);

SELECT * FROM employees ORDER BY first_name ASC;

SELECT * FROM employees ORDER BY salary DESC;

SELECT * FROM employees ORDER BY department ASC, salary DESC;