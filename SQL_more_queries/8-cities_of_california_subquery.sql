-- List all cities of california in database `hbtn_0d_usa`
SELECT cities.id, cities.name FROM states, cities WHERE states.name = 'California' ORDER BY cities.id;
