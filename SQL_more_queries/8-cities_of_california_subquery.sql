-- List all cities of california in database `hbtn_0d_usa`
SELECT cities.states_id, cities.name FROM states, cities WHERE cities.states_id = 1 ORDER BY cities.id;
