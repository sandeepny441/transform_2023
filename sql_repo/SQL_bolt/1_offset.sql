-- List the first five Pixar movies sorted alphabetically ✓
SELECT title FROM movies
ORDER BY title ASC LIMIT 5

-- List the next five Pixar movies sorted alphabetically ✓
SELECT title FROM movies
ORDER BY title ASC
LIMIT 5 OFFSET 5;

-- List all the cities west of Chicago, ordered from west to east ✓
SELECT city FROM North_american_cities
WHERE LONGITUDE < 
    (SELECT LONGITUDE FROM 
    North_american_cities 
    WHERE CITY = 'Chicago') 
order by longitude 

-- List the two largest cities in Mexico (by population) ✓
select city from North_american_cities
where country = 'Mexico'
order by population desc limit 2

-- List the third and fourth largest cities (by population) in the United States and their population 
select city from North_american_cities
where country = 'United States'
order by population desc
limit 2 offset 2