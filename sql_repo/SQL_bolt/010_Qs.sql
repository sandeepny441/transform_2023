SELECT Max(years_employed)
FROM   employees 


SELECT role,
       Avg(years_employed) AS AVG_YEARS_EMPLOYED
FROM   employees
GROUP  BY role 


SELECT building,
       Sum(years_employed)
FROM   employees
GROUP  BY building 