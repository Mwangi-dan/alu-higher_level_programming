-- Lists all genres no listed to show `Dexter`
SELECT name FROM tv_genres
RIGHT JOIN tv_show_genres ON id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_showsid
ORDER BY names;
