--  lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title FROM tv_shows
JOIN tv_show_ratings ON id = tv_show_ratings.show_id
ORDER BY tv_show_ratings.rate
