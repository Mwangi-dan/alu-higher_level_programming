-- List all cities of california in database `hbtn_0d_usa`
SELECT * FROM states WHERE name = 'California' GROUP BY cities.id;
