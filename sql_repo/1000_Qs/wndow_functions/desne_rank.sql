--1-- Write a SQL query using DENSE_RANK() to rank customers based on their creditLimit. The ranking should be such that the customer with the highest creditLimit has the rank 1.

select customerNumber, 
DENSE_RANK() over (order by creditlimit desc) as this_rank 
from customers

--2-- Write a SQL query to rank the states within each country by the total creditLimit of their customers. Use DENSE_RANK() such that the state with the highest total creditLimit within each country gets the rank 1.
select  country, state, 
DENSE_RANK() 
over (PARTITION by country order by sum(creditLimit) desc)
as temp_rank 
from customers
group by country, STATE  

--3-- Write a SQL query to rank customers within each city and country by their creditLimit. Use DENSE_RANK() so that the customer with the highest creditLimit within each city and country gets the rank 1. Remember to group by both country and city.
select country, city,
DENSE_RANK() over (PARTITION by country order by sum(creditLimit) desc) 
as temp_rank 
from customers 
group by country, city

--4-- Write a SQL query to rank customers within each country based on the total creditLimit by using the DENSE_RANK() function. The ranking should be such that the customer who has the highest total creditLimit within each country gets the rank 1. The creditLimit should be aggregated by customerNumber within each country.

select country, customerNumber, sum(creditLimit),
DENSE_RANK() over(PARTITION by country order by sum(creditLimit) desc) 
as temp_rank 
from customers
group by country, customerNumber


--5--
-- Write a SQL query to rank the countries based on the number of customers they have, using DENSE_RANK(). The country with the most customers should get a rank of 1.

select country,
DENSE_RANK() over(order by count(distinct customerName) desc) as temp_rank 
from customers
group by country

--6-- 
-- Write a SQL query using DENSE_RANK() to rank salesRepEmployeeNumber based on the number of customers they manage. The sales representative managing the most customers should have a rank of 1. Please note that salesRepEmployeeNumber can be null, so take this into account in your query.
select salesRepEmployeeNumber, 
DENSE_RANK() over(order by count(distinct customerNumber) desc)
as temp_rank 
from customers
where salesRepEmployeeNumber is not null 
group by salesRepEmployeeNumber


--7-- Write a SQL query using DENSE_RANK() to rank customers based on the sum of credit limits within each country. The customer contributing the highest sum to the credit limit within each country should be ranked as 1.
select customerName, 
DENSE_RANK() over (PARTITION by country order by creditLimit, customerName desc)
as temp_rank 
from customers

--8---- Write a SQL query using DENSE_RANK() to rank the cities within each country based on the total credit limit of their customers. The city with the highest total credit limit within each country should have a rank of 1.

select country, city,
DENSE_RANK() over (PARTITION by country order by sum(creditLimit) desc) as temp_rank 
from customers
group by country, city

--9---- Write a SQL query using DENSE_RANK() to rank customers based on their creditLimit, but within each state. The customer with the highest creditLimit within each state should have a rank of 1. Please note that states can be null, so take this into account in your query.

SELECT state, customerName, 
DENSE_RANK() over(PARTITION by state order by creditLimit desc) as 
temp_rank 
from customers 
where state is not NULL 

--10-- Write a SQL query using DENSE_RANK() to rank the customers based on their total creditLimit, but within each city. The customer with the highest total creditLimit within each city should have a rank of 1.

select city, customerName,
DENSE_RANK() over(partition by city order by creditLimit desc) 
as temp_rank 
from customers 

--11--  Write a SQL query using DENSE_RANK() to rank the countries based on the average creditLimit of their customers. The country with the highest average creditLimit should have a rank of 1.

select country, avg(creditLimit) as avg_credit_limit,
DENSE_RANK() over(order by avg(creditLimit) desc) as temp_rank 
from customers 
group by country

