--1-- Write a SQL query to divide customers into 4 groups based on their creditLimit. Each group should contain an equal number of customers. Use the NTILE function for this task.
SELECT customerName, creditLimit,
NTILE(4) OVER(ORDER BY creditLimit DESC) as quartile_rank
FROM customers

--2- Write a SQL query to divide the customers into 10 deciles based on their creditLimit. Each decile should contain an equal number of customers. Use the NTILE function for this.
select customerName, 
ntile(10) over(order by creditLimit desc) as decile_rank 
from customers 

--3 Write a SQL query to divide the customers into groups of equal sizes based on the number of customers per country. Each group should contain an equal number of countries. Use the NTILE function for this.
select country, count(customerNumber), 
NTILE(4) over(order by count(customerNumber) desc) 
as temp_Quartile from 
customers
group by country 


--4--Write a SQL query to create 5 groups of salesRepEmployeeNumbers based on the total creditLimit of customers they manage. The sales representative managing customers with the highest total creditLimit should be in the first group. Use the NTILE function in your query.
select salesRepEmployeeNumber, max(creditLimit),
NTILE(5) over(order by max(creditLimit),max(creditLimit) desc) as quantile_Rank 
from customers 
where salesRepEmployeeNumber is not null 
GROUP by salesRepEmployeeNumber

--5---- Write a SQL query that uses the NTILE function to divide the customers into 3 groups based on the sum of their credit limits, with each group containing an equal number of customers. The groups should be ordered in such a way that the group with the highest sum of credit limits is labelled as 1.

-- The resulting output should show the customerNumber, customerName, creditLimit,customerNumber, customerName, creditLimit,

select customerNumber, customerName, creditLimit,
NTILE(3) over(order by creditLimit desc) as temp_RN 
from customers 




