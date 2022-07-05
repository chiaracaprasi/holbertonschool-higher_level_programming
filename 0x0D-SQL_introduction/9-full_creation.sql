-- creates a table second_table in the database hbtn_0c_0
-- If the database exists, your script should not fail
-- The database name will be passed as an argument to the mysql command
-- You are not allowed to use the SELECT and SHOW statements
-- second_table description: id = int, name - VARCHAR(256), score = int

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table(id, name, score)
VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8)
