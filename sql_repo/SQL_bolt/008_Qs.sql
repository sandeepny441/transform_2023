SELECT Name, Role FROM employees
where Building IS NULL;

SELECT E.Building FROM EMPPLOYEES E
LEFT JOIN Buildings B
ON E.BuildinG = B.Building_name
WHERE E.ROLE IS NULL