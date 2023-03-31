-- Lists all genres of show `Dexter`
SELECT name FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.show_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_genres.name;
