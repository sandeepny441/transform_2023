-- Active: 1688557879355@@localhost@3306
-- Write a SQL subquery to find all customers whose creditLimit is less than the average creditLimit of all customers.
select customernumber, creditlimit
from customers 
where creditlimit < 
(select avg(creditlimit) from customers)


-- Write a SQL subquery to find all the salesRepEmployeeNumber who have managed customers in more than 5 different cities.
select salesRepEmployeeNumber from customers 
group by salesRepEmployeeNumber
having count(distinct city) > 5

-- find all customers who live in the city that has the highest number of customers.
select customernumber 
from customers 
where city = 
(select city from 
(select city, count(customernumber) as city_count
from customers 
group by city
order by city_count desc 
limit 1) as city_SUB_Query
)

-- Write a SQL subquery to find all customers from the city that has the lowest average creditLimit.
select customernumber from customers
where city = (
              select city from
              order by avg_credit_limit 
              (select city, avg(creditmit) as avg_credit_limit from customers
              group by city
              order by avg_credit_limit 
              limit 1) as avg_SQ
              )

-- Write a SQL subquery to find the city that has the highest number of customers with a credit limit over 50000.
select city from customers 
where city = (select city from 
(select city, count(customernumber) as cust_count
from customers 
where creditlimit > 50000
group by city
order by cust_count desc
limit 1 ) as sq_temp
)


-- Write a SQL subquery to find the salesRepEmployeeNumber who manages the customer with the highest creditLimit.
SELECT salesRepEmployeeNumber 
FROM customers 
WHERE creditLimit = (
  SELECT MAX(creditLimit) 
  FROM customers
)

-- Write a SQL subquery to find all customers who live in the same state as the customer with the highest creditLimit.

SELECT customernumber 
FROM customers 
WHERE state = (
  SELECT state 
  FROM customers 
  WHERE creditLimit = (
    SELECT MAX(creditLimit) 
    FROM customers
  )
)

-- Write a SQL subquery to find the country that has the most customers who have a creditLimit of at least 50000.

select country from customers 
where country = (select country from 
(select country, count(custmernumber) as cust_count from customers 
where creditlimit >= 50000
group by country
order by cust_count desc limit 1
) as temp_SQ
)

-- Write a SQL subquery to find the salesRepEmployeeNumber that manages the most customers in the 'USA'

select salesRepEmployeeNumber from customers 
where salesRepEmployeeNumber = 
select salesRepEmployeeNumber from
(select salesRepEmployeeNumber, count(distinct customernumber) as cust_count
from customers
where coutry = 'USA'
order by cust_count desc limit 1
)

-- Write a SQL subquery to find the city that has the most customers who have a creditLimit below 10000.
select city from customers 
where city = (select city from 
(select city, count(customernumber) as cust_count from customers 
where creditlimit < 10000
order by cust_count desc 
limit 1 
) as temp_SQ 
)

-- Write a SQL subquery to find all customers who live in the same state as the customer with the lowest creditLimit.

select customernumber from customers 
where state = (select state from cusotmers 
where creditlimit = (select min(creditlimit) from customers)
)

select customernumber from customers 
where state = (select state from  customers 
order by creditlimit 
limit 1)

-- Write a SQL subquery to find the salesRepEmployeeNumber that manages the customer with the lowest creditLimit

select salesRepEmployeeNumber from customers
where creditLimit = (select min(creditlimit) from customers)

-- Write a SQL subquery to find the customernumber of the customer who resides in the city that has the most customers.

select customernumber from customers
where city = (select city from 
(select city, count(customernumber) as cust_count
from customers 
group by city 
order by cust_count desc limit 1) 
as temp_SQ
)

-- Write a SQL subquery to find the country that has the fewest customers.
select country from customers 
where country = (select country from 
(select country, count(distinct customernumber) as cust_count
group by coutnry order by cust_count ASC
limit 1) as temp_SQ
)

-- Write a SQL subquery to find the state that has the most customers with a creditLimit above 50000.
