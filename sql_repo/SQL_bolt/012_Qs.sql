SELECT DIRECTOR, COUNT(*) FROM movies
GROUP BY DIRECTOR


SELECT director, SUM(domestic_sales + international_sales) AS Cumulative_sales_from_all_movies
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
GROUP BY director;


-- same as above
SELECT M.DIRECTOR, (B.DOMESTIC_SALES + B.INTERNATIONAL_SALES) AS TOTAL_SALES
FROM movies M
INNER JOIN Boxoffice B ON M.Id = B.MOVIE_ID
GROUP BY M.DIRECTOR;
