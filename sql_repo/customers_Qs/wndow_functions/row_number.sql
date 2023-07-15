--1--"Write a SQL query to assign a unique row number to each customer within each country, based on the ascending order of their credit limit."

select customerName, 
ROW_NUMBER() over(PARTITION by country order by customerName ASC) as temp_RN 
from customer

--2--Write a SQL query to assign a unique row number to each customer within each state, based on the descending order of their credit limit. The customer within each state with the highest credit limit should have a row number of 1.

select customerName, 
ROW_NUMBER() over(PARTITION by state order by creditLimit desc) as 
temp_RN 
from customers

--3-- Write a SQL query to assign a unique row number to each customer, based on the ascending order of their customerNumber. The customer with the smallest customerNumber should have a row number of 1.

SELECT customerName, 
ROW_NUMBER() over(order by customerNumber ASC) 
as temp_RN from customers 

-- 4 Write a SQL query that assigns a unique row number to each customer within each country, based on the descending order of their creditLimit. The customer with the highest creditLimit within each country should have a row number of 1.

select customerNumber, 
ROW_NUMBER() over(PARTITION by country order by creditLimit desc) as temp_RN from customers


--5--Write a SQL query that assigns a unique row number to each customer within each state, based on the ascending order of customerNumber. The customer with the lowest customerNumber within each state should have a row number of 1.
select customerName,  
ROW_NUMBER() over (PARTITION by state order by customerNumber ASC) as 
temp_RN from customers

--6--  Write a SQL query that assigns a unique row number to each customer within each city, based on the descending order of creditLimit. The customer with the highest creditLimit within each city should have a row number of 1.

SELECT customerNumber, 
ROW_NUMBER() over(PARTITION by city order creditlimit desc)
as temp_RN 
from customers

--7---- Write a SQL query that assigns a unique row number to each customer within each salesRepEmployeeNumber, based on ascending order of customerNumber. Remember that salesRepEmployeeNumber can be null.

SELECT customerNumber, salesRepEmployeeNumber,
ROW_NUMBER() over(partition by salesRepEmployeeNumber order by customerNumber ASC) as temp_RN 
from customers
where salesRepEmployeeNumber is NOT NULL 

--8-- Write a SQL query that assigns a unique row number to each unique customer name (customerName), based on descending order of creditLimit.

select customerNumber, 
ROW_NUMBER() over(order by creditLimit desc) as temp_RN 
from customers


--9-- Write a SQL query that assigns a row number to each row, partitioned by country and ordered by creditLimit in descending order.

select customerNUmber,
ROW_NUMBER() over(PARTITION by country order by creditLimit desc)
as temp_RN from customers

--10---- Write a SQL query that assigns a row number to each unique customerName within each city, ordered by creditLimit in descending order.

select customerName, 
ROW_NUMBER() over(PARTITION by city order by creditLimit desc) as temp_RN from customers
