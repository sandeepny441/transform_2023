SELECT DISTINCT building FROM employees;

SELECT Building_name, capacity FROM buildings
group by Building_name

SELECT DISTINCT  B.Building_name, E.role 
FROM buildings B left join Employees E
on B.Building_name = E.Building
