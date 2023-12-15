-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- lists all rows of a table by the sum of a linked row
SELECT title, SUM(tv_show_ratings.rate) as rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY title
ORDER BY rating_sum DESC;
