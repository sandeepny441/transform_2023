
SELECT M.TITLE, (B.Domestic_sales, B.International_sales)/1000000 AS GROSS_SALES
FROM MOVIES M INNER JOIN BOXOOFICE B 
ON M.ID = B.MOVIE_ID

--same as above
SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies
JOIN boxoffice
ON movies.id = boxoffice.movie_id;



SELECT M.ID, CONCAT(CAST(B.RATING * 10 AS CHAR), '%') AS RATING 
FROM MOVIES M 
INNER JOIN BOXOOFICE B
ON M.ID = B.MOVIE_ID;

--NOT exactly same as above but - same answer
SELECT title, rating * 10 AS rating_percent
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

SELECT TITLE, YEAR 
FROM MOVIES 
WHERE YEAR%2 = 0



