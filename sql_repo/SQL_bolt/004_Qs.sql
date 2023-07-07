SELECT DISTINCT(director) FROM movies
order by director;

SELECT title FROM movies
order by year desc limit 4;

SELECT title FROM movies
order by title limit 5;

SELECT title FROM movies
order by title limit 5 offset 5;