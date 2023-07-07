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



