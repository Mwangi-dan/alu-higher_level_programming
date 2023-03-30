-- List all cities of california in database `hbtn_0d_usa`
SELECT cities.id, cities.name FROM states, cities WHERE cities.state_id = 1 ORDER BY cities.id;
