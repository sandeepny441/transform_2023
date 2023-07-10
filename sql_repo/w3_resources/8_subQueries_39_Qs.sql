--1 
select s.*, c.* 
from salesman s 
inner join  
customer c 
where s.customer_id = c.customer_id
having s.salesman_name = 'Paul'
-- OR whre s.salesman_name = 'Paul'
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE name = 'Paul Adam')

--2
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE city = 'London')

--3
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE CUSTOMER_ID = '3007')

--4
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE PRUCH_AMT >  
    (SELECT avg(pruch_amt) FROM salesman where ord_date = '10, october, 2022') 

