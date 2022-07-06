-- creates a table called force_name in MySQL server
-- description id = INT, name = VARCHAR(256) can't be null
-- The database name will be passed as an argument of the mysql command
-- If the database exists, your script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
