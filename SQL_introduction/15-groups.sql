-- Lists the number of records wuth the same score in `second_table`
SELECT score, COUNT(score) as number FROM second_table GROUP BY score HAVING number >= 1;
