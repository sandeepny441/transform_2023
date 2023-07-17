--1--- Write a SQL query using the LAG function to retrieve the previous customer's name for each row, ordered by customerNumber. This can be used to see which customer was added just before the current one.

select customerName, 
LAG(customerName) over(order by customerNumber ASC) as prev_cust_name
from customers


--2---- Write a SQL query using the LAG() function to fetch the previous sales representative number for each row when the data is ordered by salesRepEmployeeNumber in ascending order. This could be useful for comparing customer data managed by different sales representatives.

SELECT 
  customerName, 
  salesRepEmployeeNumber,
  LAG(salesRepEmployeeNumber) OVER (ORDER BY salesRepEmployeeNumber ASC) AS prev_sales_rep
FROM customers
WHERE salesRepEmployeeNumber IS NOT NULL;


--3--  Write a SQL query using the LAG() function to fetch the previous customer's creditLimit for each row when the data is ordered by creditLimit in descending order. This can help in determining how the creditLimit changes from one customer to another.

select customername, 
lag(creditlimit, 1, 200000) over(order by creditlimit desc) as prev_cust_credit_limit 
from customers

--4-- Write a SQL query using the LAG() function to fetch the previous customer's city for each row when the data is ordered by customerNumber in ascending order.

select  customerName, city, 
lag(city) over(order by customerNumber desc) as prev_cust_city 
from customers

--5-- Write a SQL query using the LAG() function to fetch the previous customer's country for each row when the data is ordered by customerName in ascending order.

select customerName,
lag(country) over (order by customerName ASC) as prev_cust_country 
from customers 



