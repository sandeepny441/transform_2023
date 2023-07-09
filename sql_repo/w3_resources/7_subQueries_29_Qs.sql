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
order by orders.ord_date desc

