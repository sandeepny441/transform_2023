--1--  Write a SQL query to rank customers based on their creditLimit, with the customer having the highest creditLimit ranked as 1.
select customernumber, 
rank() over (order by creditlimit desc) as credit_rank 
from customers 

--2-- Write a SQL query to rank customers within each country, based on their creditLimit. The ranking should be such that the customer with the highest creditLimit within each country gets the rank 1.
select country, creditlimit, customernumber,
rank() over (partition by country order by creditlimit desc) as credit_rank 
from customers 

--3-- Write a SQL query to rank states by the number of customers they have, with the state having the most customers ranked as 1.
select state,  
rank() over(order by cust_count desc) as state_rank 
from (select state, count(customernumber) as cust_count from customers
group by state) as temp_SQ_state_counts

--4-- Write a SQL query to rank customers within each state by their creditLimit, with the customer having the highest creditLimit within each state ranked as 1.
select customernumber, 
rank() over (partition by state order by creditlimit desc) as state_rank 
from customers

--5-- Write a SQL query to rank salesRepEmployeeNumbers by the total creditLimit of customers they manage. The sales representative managing customers with the highest total creditLimit should be ranked as 1.

SELECT salesRepEmployeeNumber, sum(creditlimit) as x,
rank() over(order by sum(creditlimit) desc ) as credit_rank 
from customers
group by salesRepEmployeeNumber

--6-- Write a SQL query to rank customers within each country and state by their creditLimit, with the customer having the highest creditLimit within each country and state ranked as 1. The result should also include the customers' country, state, and creditLimit.

select country, state, creditlimit, 
rank() over(partition by country, state order by creditLimit desc)
as this_rank 
from customers

--7-- Write a SQL query to rank the sales representatives by the number of customers they manage, with the sales representative managing the most customers ranked as 1.

select salesRepEmployeeNumber,count(DISTINCT customerNumber),
rank() over (order by count(DISTINCT customerNumber) desc) as this_Rank 
from customers
where salesRepEmployeeNumber is not null 
group by salesRepEmployeeNumber

--8-- Write a SQL query to rank countries by the total credit limit of all customers from each country, with the country having the highest total credit limit ranked as 1.

select country, 
rank() over (order by sum(creditLimit) desc) as this_rank
from customers 
group by country


--9-- Write a SQL query to rank customers within each country based on their credit limit, but only for customers who have a sales representative assigned to them. The customer with the highest credit limit within each country should be ranked as 1.
select customerNumber, country, creditLimit,
rank() over(partition by country order by creditLimit desc) as this_rank from customers 
where salesRepEmployeeNumber is not null 

--10-- Write a SQL query to rank cities within each country by the total credit limit of their customers. The city with the highest total credit limit within each country should be ranked as 1.

select country, city,  
rank() over (partition by country order by sum(creditLimit) desc) as this_rank 
from customers
group by country, city


