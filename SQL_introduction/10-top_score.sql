-- List all records of table `second_table`
SELECT score, name, COUNT(*)
FROM second_table
GROUP BY score;
