--1
SELECT salesman_id,
       NAME,
       city,
       Concat(commission, '%') AS commission
FROM salesman; 

--2 From the following table, write a SQL query to find the number of orders booked for each day. Return the result in a format like "For 2001-10-10 there are 15 orders".". 
SELECT ' For',
       ord_date,
       ',there are',
       Count (ord_no),
       'orders.'
FROM   orders
GROUP  BY ord_date; 

SELECT Concat('For ', ord_date, ', there are ', Count(ord_no), ' orders.') AS
       result
FROM   orders
GROUP  BY ord_date; 

--3 
SELECT * FROM ORDERS
ORDER BY ORDER_NO 

--4 
SELECT * FROM ORDERS
ORDER BY ORD_DATE DESC

--5 
SELECT * FROM ORDERS
ORDER BY ORD_DATE, PURCH_AMT DESC

--6
SELECT * FROM customer_id
ORDER BY customer_id

--7 
SELECT SALESMAN_ID, ORD_DATE, MAX(PURCH_AMT) 
FROM ORDERS 
GROUP BY SALESMAN_ID, ORD_DATE
ORDER BY SALESMAN_ID, ORD_DATE 

--8 
SELECT * FROM CUSTOMER
ORDER BY CITY DESC

--9
SELECT CUSTOMER_ID, COUNT(DISTNCT ORD_NO), MAX(PURCH_AMT)
FROM ORDERS
GROUP BY CUSTOMER_ID

--10 
SLECT ORD_DATE, SUM(PURCH_AMT), SUM(PURCH_AMT) * 0.15 AS TOTAL_COMMISION
FROM ORDERS 
GROUP BY ORD_DATE
ORDER BY ORD_DATE 




