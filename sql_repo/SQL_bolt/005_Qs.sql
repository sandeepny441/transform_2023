SELECT * FROM north_american_cities
where country = 'Canada'

SELECT City, Latitude from North_american_cities 
where country = 'United States'
order by Latitude desc

SELECT City from North_american_cities 
where Longitude < (select min(longitude) 
 form North_american_cities where city = 'Chicago')
order by Longitude 

SELECT CITY FROM NORTH_american_cities
WHERE COUNTRY = 'Mexico'
ORDER BY POPULATION DESC 
LIMIT 2

SELECT CITY FROM NORTH_american_cities
WHERE COUNTRY = 'United States'
ORDER BY POPULATION DESC 
LIMIT 2 offset 2

