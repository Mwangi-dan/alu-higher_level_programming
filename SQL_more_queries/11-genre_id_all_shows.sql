-- Lists all shows contained in the database `hbtn_0d_tvshows`
-- If show doesnt have a genre, it displays NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_shows_genres.genre_id
