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
select * from orders o
where purch_amt > (select avg(purch_amt) from custoemrs c 
                  where o.customer_id = c.customer_id)

--14 
select o.sum(purch_amt) as final_purch_amt 
group by o.order_date
where ord_date in (select ord_date, max(purch_amt) from orders 
group by ord_date
having o.sum(purch_amt) > max(purch_amt) + 100000
)

--15
select * from customer
where ((select count(city) from customer where city =  'London') > 1)  
--BETTER 
SELECT *
FROM customer
WHERE EXISTS (
    SELECT *
    FROM customer
    WHERE city = 'London'
)

--16
SELECT salesman_id, name, city, commission
FROM salesman
WHERE salesman_id IN (
    SELECT salesman_id
    FROM customer
    GROUP BY salesman_id
    HAVING COUNT(customer_id) > 1
)

--17 
SELECT salesman_id, name, city, commission
FROM salesman
WHERE salesman_id IN (
    SELECT salesman_id
    FROM customer
    GROUP BY salesman_id
    HAVING COUNT(customer_id) = 1
)

--18 
SELECT salesman_id
FROM salesman
WHERE salesman_id IN (
    SELECT salesman_id
    FROM customer
    WHERE salesman_id IN (
        SELECT salesman_id
        FROM orders
        GROUP BY salesman_id
        HAVING COUNT(ord_id) > 1
    )
)
--19 
select salesman_id from 
salesman where salesman_id in 
(select salesman_id from customer 
where salesman.city = customer.city)

--20 
SELECT salesman_id, name, city, commission
FROM salesman
WHERE city IN (
    SELECT DISTINCT city
    FROM customer
)

--21 
select salesman_name from 
salesman where salesman_name < 
ANY (select customer_name from customer)

--22
select * from customers 
where grade > ALL (select grade from customers
where customer.city > 'New York')

--23 
select ord_no from orders 
where purch_amt > ANY (select purch_amt from orders 
where ord_date = 'Sept 5, 2022')

--24 
select ord_no from orders 
where purch_amt < ANY
(select purch_amt from orders 
where city = 'LONDON')

--25
select ord_no from orders 
where purch_amt < ANY 
(select max(purch_amt) from orders 
where orders.customer_id = customer.customer_id
AND where city = 'LONDON')

--26 
select * from customer 
where grade > All (select grade from customer
where city = 'New York')

--27 
select sum(purch_amt) from orders o
inner join salesman c
ON o.salesman_id = c.salesman_id 
WHERE s.city = c.city
and where s.city in (select distinct city from customer)
 
--28 
select * from customer 
where grade NOT IN  (select grade from customer 
where city = 'LONDON' and grade IS NOT  null )

--29 
select * from customer 
where grade NOT IN  (select grade from customer 
where city = 'PARIS' and grade IS NOT  null )

select * from customer 
where grade <> ALL  (select grade from customer 
where city = 'PARIS' and grade IS NOT  null )

select * from customer 
where grade <>  (select grade from customer 
where city = 'PARIS' and grade IS NOT  null )


--30 







