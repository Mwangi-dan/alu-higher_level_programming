-- List all cities of california in database `hbtn_0d_usa`
SELECT * FROM STATES WHERE name = 'California' GROUP BY cities.id;
