-- Lists all shows contained in `hbtn_0d_tvshows`
-- Each record should display `tv_shows.title and `tv_show_genres.genre.id`
SELECT * FROM tv_shows
FULL JOIN tv_shows
ON `tv_shows.id` = `tv_show_genres.show_id`

