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