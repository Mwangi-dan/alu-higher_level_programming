-- Lists all shows without genre `Comedy`
SELECT title FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id NOT IN (
	SELECT tv_show_genres.genre_id FROM tv_show_genres
	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres <> 'Comedy' )
ORDER BY title;
