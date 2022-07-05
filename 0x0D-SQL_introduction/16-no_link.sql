-- lists all records of the table second_table of the database
-- Don’t list rows without a name value
-- Result should display score and name in this order
-- Records should be listed by descending order
-- The database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
