-- Lists that lists all cities in database `hbtn_0d_usa`
SELECT cities.id, cities.name, states.name FROM cities, states ORDER BY cities.id;
