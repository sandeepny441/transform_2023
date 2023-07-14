-- Write a SQL query to rank customers based on their creditLimit, with the customer having the highest creditLimit ranked as 1.
select customernumber, 
rank() over (order by creditlimit desc) as credit_rank 
from customers 

-- Write a SQL query to rank customers within each country, based on their creditLimit. The ranking should be such that the customer with the highest creditLimit within each country gets the rank 1.
select country, creditlimit, customernumber,
rank() over (partition by country order by creditlimit desc) as credit_rank 
from customers 

-- Write a SQL query to rank states by the number of customers they have, with the state having the most customers ranked as 1.
select state, customers, 
rank() over(order by cust_count desc) as state_rank 
from (select state, count(cusotmernumber) cust_count from customers
group by state) as temp_SQ_state_counts

-- Write a SQL query to rank customers within each state by their creditLimit, with the customer having the highest creditLimit within each state ranked as 1.
select cusotmernumber, 
rank() over (partition by state order by creditlimit desc) as state_rank 
from customers

-- Write a SQL query to rank salesRepEmployeeNumbers by the total creditLimit of customers they manage. The sales representative managing customers with the highest total creditLimit should be ranked as 1.



