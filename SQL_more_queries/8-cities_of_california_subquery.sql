-- List all cities of california in database `hbtn_0d_usa`
SELECT states.id, cities.name FROM states, cities WHERE states.id = 1 ORDER BY cities.id;
