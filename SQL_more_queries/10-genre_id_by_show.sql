-- Lists all shows contained in `hbtn_0d_tvshows`
-- Each record should display `tv_shows.title and `tv_show_genres.genre.id`
SELECT * FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id
UNION ALL
SELECT * FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.id IS NULL
