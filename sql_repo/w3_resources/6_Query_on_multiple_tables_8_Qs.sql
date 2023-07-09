--1 
SELECT S.NAME, C.NAME, S.CITY 
FROM SALESMAN S 
INNER JOIN CUSTOMER C 
ON S.CITY = C.ITY 

--2 
SLEECT C.CUST_NAME, S.SALESMAN_NAME
FROM CUSTOMER C 
INNER JOIN SALESMAN S
ON C.SALESMAN_ID = S.SALESMAN_ID

--3 From the following tables, write a SQL query to find those salespeople who generated orders for their customers but are not located in the same city. Return ord_no, cust_name, customer_id (orders table), salesman_id (orders table).  

--3 
SELECT ord_no, cust_name, orders.customer_id, orders.salesman_id
FROM salesman, customer, orders
WHERE customer.city <> salesman.city
AND orders.customer_id = customer.customer_id
AND orders.salesman_id = salesman.salesman_id;

--4 From the following tables, write a SQL query to locate the orders made by customers. Return order number, customer name.  

SELECT ORD_NO, cust_name
FROM ORDERS, CUSTOMER 
WHERE ORDERS.customer_id = CUSTOMER.customer_id

--5 
select cust_id, grade 
from 
customer, salesman, orders 
where customer.cust_id = orders.customer_id
customer.salesmand_id = salesman.salesmand_id 
and orders.grade is not null 
and salesman.sale_id i not null 


--6 
SELECT cusrtomer.cust_name, salesman.salesman_name 
from cusrtomer, salesman 
where customer.salesman = salesman.salesman_id 
and salesman.commision between 0.12 and 0.14

--7 
select salesman.purch_amt *commision, ord_no
from salesman, customer, orders 
where customer.salesman_id = order.customer_id 
and 
salesman.salesman_id = orders.salesman_id
and 
customer.grade > 200 

--8 
select customer.customer_id, customer.salesman, orders.ord_date 
from customer, salesman, orders
where customer.cust_id = orders.cust_id 
and 
order.ord_date > '2022-01-01'



