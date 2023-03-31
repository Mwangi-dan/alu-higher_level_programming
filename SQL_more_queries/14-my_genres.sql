-- Lists all genres of show `Dexter`
SELECT name FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_genres.id
ORDER BY tv_genres.name;
