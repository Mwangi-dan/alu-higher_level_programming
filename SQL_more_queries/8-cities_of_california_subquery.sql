-- List all cities of california in database `hbtn_0d_usa`
SELECT * FROM cities WHERE states.name = 'California' ORDER BY cities.id;
