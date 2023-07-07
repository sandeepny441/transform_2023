SELECT M.title,
       B.domestic_sales,
       B.international_sales
FROM   movies M
       INNER JOIN boxoffice b
               ON M.id = B.movie_id 

SELECT M.title,
       B.domestic_sales,
       B.international_sales
FROM   movies M
       INNER JOIN boxoffice b
               ON M.id = B.movie_id
WHERE  B.international_sales > B.domestic_sales 

SELECT M.title,
       B.domestic_sales,
       B.international_sales
FROM   movies M
       INNER JOIN boxoffice b
               ON M.id = B.movie_id
ORDER  BY B.rating DESC 