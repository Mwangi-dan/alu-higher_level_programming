-- omputes the score average of all records in the table `second_table`
ALTER TABLE second_table ADD average (SELECT AVG(score) FROM second_table);
