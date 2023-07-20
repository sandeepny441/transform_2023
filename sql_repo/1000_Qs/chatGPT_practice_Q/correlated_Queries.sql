--1-- Write a correlated subquery to find all customers whose creditLimit is higher than the average creditLimit of customers in the same country
select * from customers c1
where creditLimit > 
(select avg(creditLimit) from customers c2
 where c1.country = c2.country)

--2--  Write a correlated subquery to find the customerName of customers who are the only customer in their country (i.e., their country only has one customer).

select customerName from customers c1
where 1 = (select count(*) from customers c2 
where c1.country = c2.country)

--3-- Write a correlated subquery to find the names of customers who live in a state where the total number of customers is more than 10.
select customerName from customers 
where state IN  (select state from customers
group by state
having count(distinct customerNumber) > 10 )

select * from customers c1 
where 10 < (select count(*) from customers c2 
where c1.state = c2.state)

--4-- Write a correlated subquery to find customers who have the highest creditLimit in their country.
select customerName from customers c1 
where creditLimit = (select max(creditLimit) 
from customers c2 
where c1.country = c2.country)

--5- Write a correlated subquery to find the customerName of customers who have the same salesRepEmployeeNumber as at least one other customer in a different country.
select customerName from customers c1 
where salesRepEmployeeNumber = 
(select salesRepEmployeeNumber from customers c2 
where c1.salesRepEmployeeNumber = c2.salesRepEmployeeNumber
AND c1.country <> c2.country)

--6-- Write a correlated subquery to find all salesRepEmployeeNumbers who are responsible for customers in more than two different countries.

select salesRepEmployeeNumber from customers c1
where 2 < (select count(distinct country) from customers c2 
where c1.salesRepEmployeeNumber = c2.salesRepEmployeeNumber)