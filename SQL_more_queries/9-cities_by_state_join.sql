-- Lists that lists all cities in database `hbtn_0d_usa`
SELECT cities.id cities.name states.name FROM states, cities ORDER BY cities.id;
