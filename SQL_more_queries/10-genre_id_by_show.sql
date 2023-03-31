-- Lists all shows contained in `hbtn_0d_tvshows`
-- Each record should display `tv_shows.title and `tv_show_genres.genre.id`
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
FULL JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;
