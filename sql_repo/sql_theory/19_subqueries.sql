SELECT column1, column2
FROM table1
WHERE column2 IN (SELECT column2 FROM table2);


SELECT t1.column1, t2.column2
FROM (SELECT column1 FROM table1 WHERE condition) AS t1
JOIN (SELECT column2 FROM table2 WHERE condition) AS t2
ON t1.id = t2.id;
