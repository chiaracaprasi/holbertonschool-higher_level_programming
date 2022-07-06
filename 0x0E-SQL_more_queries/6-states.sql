-- creates a table called id_not_null in MySQL server
-- description id = INT default value 1, name = VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the database exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL
);
