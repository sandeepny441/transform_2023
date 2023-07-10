--1 
select s.*, c.* 
from salesman s 
inner join  
customer c 
where s.customer_id = c.customer_id
having s.salesman_name = 'Paul'
-- OR whre s.salesman_name = 'Paul'
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE name = 'Paul Adam')

--2
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE city = 'London')

--3
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE CUSTOMER_ID = '3007')

--4
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE PRUCH_AMT >  
    (SELECT avg(pruch_amt) FROM salesman where ord_date = '10, october, 2022') 

--5 
SELECT ord_no, purch_amt, ord_date, customer_id, salesman_id
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE city = 'New York City')

--6
SELECT commision
FROM orders
WHERE salesman_id = 
    (SELECT salesman_id FROM salesman WHERE city = 'Paris')


--7 
select * from customer 
where salesman_id = 
(select salesman_id from salesman where salesman_name = 'Mc Lyon')

--8 
select grade, count(grade)
from customer 
where grade > (select avg(grade) from customers where city = 'NY')

--9 
select salesman_name
from salesman
where commission =  (select max(commision) from orders) 

--10 
select * from customer 
where customer_id in 
(select customer_id from orders where ord_date = "2022-10-20")

--11 
select salesman_id 
from salesman
where salesman in (select salesman from customer 
                  group by salesman
                  having count(customer_id) > 

--12 
select * from orders o
where purch_amt > (select max(purch_amt) from custoemrs c 
                  where o.customer_id = c.customer_id)
                  
--13 
select * from orders o
where purch_amt > (select avg(purch_amt) from custoemrs c 
                  where o.customer_id = c.customer_id)

--14 
select o.sum(purch_amt) as final_purch_amt 
group by o.order_date
where ord_date in (select ord_date, max(purch_amt) from orders 
group by ord_date
having o.sum(purch_amt) > max(purch_amt) + 100000
)

--15
select * from customer
where ((select count(city) from customer where city =  'London') > 1)  
--BETTER 
SELECT *
FROM customer
WHERE EXISTS (
    SELECT *
    FROM customer
    WHERE city = 'London'
)

--16
SELECT salesman_id, name, city, commission
FROM salesman
WHERE salesman_id IN (
    SELECT salesman_id
    FROM customer
    GROUP BY salesman_id
    HAVING COUNT(customer_id) > 1
)

--17 
SELECT salesman_id, name, city, commission
FROM salesman
WHERE salesman_id IN (
    SELECT salesman_id
    FROM customer
    GROUP BY salesman_id
    HAVING COUNT(customer_id) = 1
)

--18 
SELECT salesman_id
FROM salesman
WHERE salesman_id IN (
    SELECT salesman_id
    FROM customer
    WHERE salesman_id IN (
        SELECT salesman_id
        FROM orders
        GROUP BY salesman_id
        HAVING COUNT(ord_id) > 1
    )
)
--19 
select salesman_id from 
salesman where salesman_id in 
(select salesman_id from customer 
where salesman.city = customer.city)

--20 
SELECT salesman_id, name, city, commission
FROM salesman
WHERE city IN (
    SELECT DISTINCT city
    FROM customer
)

--21 
select salesman_name from 
salesman where salesman_name < 
ANY (select customer_name from customer)

--22
select * from customers 
where grade > ALL (select grade from customers
where customer.city > 'New York')

--23 
select ord_no from orders 
where purch_amt > ANY (select purch_amt from orders 
where ord_date = 'Sept 5, 2022')

--24 
select ord_no from orders 
where purch_amt < ANY
(select purch_amt from orders 
where city = 'LONDON')

--25
select ord_no from orders 
where purch_amt < ANY 
(select max(purch_amt) from orders 
where orders.customer_id = customer.customer_id
AND where city = 'LONDON')

--26 
select * from customer 
where grade > All (select grade from customer
where city = 'New York')

--27 
select sum(purch_amt) from orders o
inner join salesman c
ON o.salesman_id = c.salesman_id 
WHERE s.city = c.city
and where s.city in (select distinct city from customer)
 
--28 
select * from customer 
where grade NOT IN  (select grade from customer 
where city = 'LONDON' and grade IS NOT  null )

--29 
select * from customer 
where grade NOT IN  (select grade from customer 
where city = 'PARIS' and grade IS NOT  null )

select * from customer 
where grade <> ALL  (select grade from customer 
where city = 'PARIS' and grade IS NOT  null )

select * from customer 
where grade <>  (select grade from customer 
where city = 'PARIS' and grade IS NOT  null )

--30 
select * from customer 
where grade NOT IN  (select grade from customer 
where city = 'DALLAS' and grade IS NOT  null )

--31 
select c.com_name, i.avg(pro_price)
from company_mast c inner join item_mast i 
group by c.com_name 
where c.com_id = i.pro_com

--32
select c.pro_name, avg(i.pro_price) as avg_price
from item_mast i 
inner join c 
where i.pro_com = c.com_id 
group by i.pro_name 
having avg_price > 350

--33
select i.pro_com, max(c.pro_price)
from company_mast c 
inner join item_mast i 
where i.pro_com = c.pro_id 
group by i.pro_com 

--OR 
SELECT P.pro_name AS "Product Name", 
       P.pro_price AS "Price", 
       C.com_name AS "Company"
   FROM item_mast P, company_mast C
   WHERE P.pro_com = C.com_id
     AND P.pro_price =
     (
       SELECT MAX(P.pro_price)
         FROM item_mast P
         WHERE P.pro_com = C.com_id
     );

--34 
select * from emp_details
where EMP_LNAME IN ('Gabriel', 'Dosio')

--35 
select * from emp_details
where emp_dept IN (89, 63)

--36
select * from emp_details
where emp_dept IN (select dept_no from emp_department 
                  where DPT_ALLOTMENT > 50000)

--37 
select * from emp_department
where DPT_ALLOTMENT > (select avg(DPT_ALLOTMENT) from emp_department) 

--38 
select dept_no from emp_department
where dept_no in (select dept_no from emp_details
group by dept_no,
 having count(count(distinct emp_id) > 2))

select dept_no, count(distinct emp_id) as emp_count_by_dept 
from emp_details
group by dept_no 
having emp_count_by_dept > 2

--39 
select dept_no from dept_details 
order by dept_allocation DESC 
limit 1 offset 1 

select dept_no from dept_details
where dept_no in 
(select dept_no from dept_details 
order by dept_allocation limit 1 offset 1 
)

select dept_no from dept_details
where dept_no in 
(select dept_no in dept_details 
where dept_allocation < min(dept_allocation) 
where dept_allocation > 
(select min(dept_allocation) from dept_detials))









