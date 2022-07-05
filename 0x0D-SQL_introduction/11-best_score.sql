-- lists all rows of the table first_table from the database
-- The database name will be passed as an argument of the mysql command
-- All fields should be printed

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
