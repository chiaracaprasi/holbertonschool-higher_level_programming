-- lists the number of records with the same score in the table second_table
-- Result should display score, #of records for score with the label number
-- The database name will be passed as an argument of the mysql command

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;
