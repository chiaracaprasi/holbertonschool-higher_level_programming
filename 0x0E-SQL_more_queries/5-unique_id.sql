-- creates a table called unique_id in MySQL server
-- description id = INT default value 1 and unique, name = VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the database exists, your script should not fail

CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
