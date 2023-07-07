--1
SELECT * FROM customer
WHERE GRADE > 100

--2
SELECT * FROM customer
WHERE GRADE > 100
AND
CITY = "NEW YORK"

--3
SELECT * FROM customer
WHERE GRADE > 100
OR
CITY = "NEW YORK"

--4
SELECT * FROM customer
WHERE GRADE <= 100
OR
CITY = "NEW YORK"

--5
SELECT * FROM customer
WHERE GRADE <=  100
OR
CITY <> "NEW YORK"
--same 
SELECT * 
FROM customer 
WHERE NOT (city= 'New York' OR grade>100);

--6 
SELECT * FROM ORDERS
WHERE ord_date <> '2012-09-10'
OR salesman_id <> 5005 
OR purch_amt <= 1000
--same as above
SELECT * FROM ORDERS
EXCEPT
SELECT * FROM ORDERS
WHERE ord_date = '2012-09-10'
  AND salesman_id = 5005
  AND purch_amt > 1000;

--7 
SELECT * FROM salesman
WHERE commission BETWEEN 0.10 AND 0.12

--8 
SELECT * FROM ORDERS
WHERE (PURCH_AMT < 200 
OR (ORD_DATE > '2012-02-10'
AND customer_id < 3009))

--9 
SELECT * FROM ORDERS
WHERE (ORD_DATE =  '2012-08-17' 
OR (customer_id  > '3005'
AND PURCH_AMT < 1000))

--10 
SELECT ord_no,purch_amt, 
(100*purch_amt)/6000 AS "Achieved %", 
(100*(6000-purch_amt)/6000) AS "Unachieved %" 
FROM  orders 
WHERE (100*purch_amt)/6000>50;

--11
SELECT *
FROM emp_details
WHERE emp_lname IN ('Dosni', 'Mardy');

--12
SELECT *
FROM emp_details
WHERE EMP_DEPT IN (47, 63);

--13








