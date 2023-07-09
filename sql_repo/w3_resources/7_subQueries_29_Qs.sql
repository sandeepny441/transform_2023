--1
select salesman.name and customer.cust_name
from salesman inner join customer 
where salesman.city = customer.city 

--2
select custome.cust_name, orders.ord_no, ord.purch_amt
from customer inner join orders 
where customer.cust_id = orders.ord_id 

--3 
select * from customer inner join salesman 
where customer.salesman_id = salesman.salesman_id 

--4 
select customer.cust_name, customer.city 
from customer inner join salesman 
where customer.salesman_id = customers.salesman_id
and salesman.commission < 0.12 

--5 
select salesman.salesman_id 
from salesman inner join customer 
where salesman.salesman_id = customers.salesman_id
and salesman.commission > 0.12 
and salesman.city <> customer.city 

--6 
seelct * from customer, salesman, orders 
where order.cust_id = customer.cust_id 
and salesman.salesman_id = customer.salesman_id 
and orders.salesman_id = salesman.salesman_id
--OR
select * from cusrtomer inner join orders 
where customer.salesman_id = orders.salesman_id
inner join salesman where 
orders.salesman_id = salesman.salesman_id

--7 
select * from orders
natual join salesman
natural join customer 

-- If both product_id and customer_id exist in both tables and you use a NATURAL JOIN, the SQL engine will treat both columns as join conditions. This means that a row will only be included in the result set if both the product_id and customer_id in that row match between the two tables.

--8
seelct * from customer
inner join salesman
where customer.salesman_id = salesman.salesman_id
order by customer.customer_id ASC

--9 
seelct * from customer
inner join salesman
where customer.salesman_id = salesman.salesman_id
and customer.grade < 300
order by customer.customer_id ASC

--10 
seelct * from customer
inner join orders
where customer.customer_id = orders.customer_id
order by orders.ord_date

--11 
select * from cusotmers 
left outer join orders 
where customer.cust_id = orders.cust_id 
left outer join salesman
where orders.salesman_id = salesman.salesman_id

--12 
select s.salesman_id from salesman 
left outer join customer c
on s.salesman_id = c.salesman_id 

--13 
SELECT a.cust_name,a.city,a.grade, 
b.name AS "Salesman", 
c.ord_no, c.ord_date, c.purch_amt 
FROM customer a 
RIGHT OUTER JOIN salesman b 
ON b.salesman_id=a.salesman_id 
RIGHT OUTER JOIN orders c 
ON c.customer_id=a.customer_id;


--14 Write a SQL statement to make a list for the salesmen who either work for one or more customers or yet to join any of the customer. The customer, may have placed, either one or more orders on or above order amount 2000 and must have a grade, or he may not have placed any order to the associated supplier.

select * from customer c 
full right join salesman s
ON c.salesman_id = s.salesman_id 
left join orders o
where o.customer_id  = c.customer_id 

--15 
select * from customers 
full left join orders 
ON c.customer_id = o.customer_id

--16
SELECT a.cust_name,a.city, b.ord_no,
b.ord_date,b.purch_amt AS "Order Amount" 
FROM customer a 
FULL OUTER JOIN orders b 
ON a.customer_id=b.customer_id 
WHERE a.grade IS NOT NULL;
-- # DOUBT 

--17 


































