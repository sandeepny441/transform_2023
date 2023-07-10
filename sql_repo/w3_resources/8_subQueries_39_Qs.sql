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

--5 
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE city = 'New York City')

--6
SELECT commision
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE city = 'Paris')


--7 
select * from customer 
where salesman_id = 
(select salesman_id from salesman where salesman_name = 'Mc Lyon')

--8 
select grade, count(grade)
from customer 
where grade > (select avg(grade) from customers where city = 'NY')

--9 
select salesman_name
from salesman
where commission =  (select max(commision) from orders) 

--10 
select * from customer 
where customer_id in 
(select customer_id from orders where ord_date = "2022-10-20")

--11 
select salesman_id 
from salesman
where salesman in (select salesman from customer 
                  group by salesman
                  having count(customer_id) > 

--12 
select * from orders o
where purch_amt > (select max(purch_amt) from custoemrs c 
                  where o.customer_id = c.customer_id)

--13 

