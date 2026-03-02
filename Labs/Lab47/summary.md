# Introduction to Databases & PostgreSQL (lab 47 summary)
A **database** is an organized collection of structured data that allows
efficient storage, retrieval, and management of information.

Databases are used in:
- Web applications
- Financial systems
- Inventory management
- User authentication systems

## Databases using
- Data is stored permanently (unlike RAM).
- Fast searching, sorting, and filtering using queries.
- Handles large datasets and many users.
- Ensures consistency using constraints (primary keys, foreign keys).
- Supports authentication and role-based access control.

## PostgreSQL
**PostgreSQL** is a powerful open-source relational database system.

Benefits:
- Reliable and safe transactions.
- Custom data types and functions.
- JSON support, indexing, full-text search.
- Works on Windows, macOS, Linux.

## Working with psql (CLI)
**Login:** `psql -U postgres`

**Exit:** `\q`

### Useful Commands
- List databases: `\l`
- Connect to database: `\c dbname`
- List tables: `\dt`
- List users: `\du`

## Creating a Database
sql:
- Create database: `CREATE DATABASE mydb;`
- Create user: `CREATE USER myuser WITH PASSWORD 'password';`
- Grant permissions: `GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;`
- Creating a Table: <pre>```CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);```</pre>
- Insert data: <pre>```
INSERT INTO users (name, email)
VALUES ('John', 'john@example.com');```</pre>
- Query data: `SELECT * FROM users;`

## Where PostgreSQL Is Used
- Web Development
- Data Analytics
- Financial Systems
- Content Management Systems (CMS)