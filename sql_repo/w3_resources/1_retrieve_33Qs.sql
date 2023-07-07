---==========================================================================
-- salesnam
---==========================================================================
--1 
select *
from salesman

--2 
select "print any string"

--3 
select 12, 23, 43 

--4 
select 10 + 23 

--5 any arithmentic expression 
select 1- + 23 + 43 * 43 

--6 
select names and commissions
from salesman

--7 
select ord_date, salesman_id, ord_no, purch_amt 
from salesman 

--8 
select distinct(salesman_id)
 from salesman

 --9 
select name, city from salesman
where city = 'Paris' 

--10 
select customer_id, cust_name, city, grade, salesman_id
from salesman 
where grade = 200 

--11 
select ord_no, ord_date, purch_amt
from salesman 
where ord_no = 5001 
---==========================================================================
-- nobel_win
---==========================================================================
--12 
select year, subject, winner
from nobel_win
where year = 1970 

--13 
select year, subject, winner
from nobel_win
where year = 1970
and 
subject = 'Literature'

--14 
select year, subject 
from nobel_win
where winner = 'Dennis Gabor'

--15 
select winner
from nobel_win
where year = 1950 
and 
subject = 'Physics'

--16 
select year, subject, winner, country 
from nobel_win
where 1965 <= year <= 1975

--17 
SELECT * FROM nobel_win
 WHERE year >1972
  AND winner IN ('Menachem Begin',
                  'Yitzhak Rabin');

--18 
select year, subject, winner, country, category
from salesman
where WINNER LIKE 'Louis %'

--19 
select year, subject, winner, country, category
from salesman
where (year = 1970 and subject = 'Physics')
OR 
(year = 1971 and subject = 'Economics')

--20 
select year, subject, winner, country,  category
from nobel_win
where year=1970
and 
where subject not in ('Physiology', 'Economics')

--21
select  year, subject, winner, country,  categoryf
from nobel_win
where (year < 1970 and subject = 'Physiology')
UNION 
select  year, subject, winner, country,  categoryf
from nobel_win
where (year >= 1971 and subject = 'Peace')

--22
select  year, subject, winner,  category
from nobel_win
where (year < 1970 and subject = 'Physiology')
UNION 
select  year, subject, winner, country,  categoryf
from nobel_win
where (year >= 1971 and subject = 'Peace')


--23 
select year, subject, winner, country,  category
from nobel_win
where SUBJECT not like 'P%'
order by year desc 

--24 
SELECT * FROM NOBLE_WIN
WHERE YEAR = 1970
ORDER BY 
CASE 
  WHEN SUBJECT IN ('Economics', 'Chemistry') then 1 
  esle 0 
END 
  -- asc
  -- asc, subject
  asc, subject, winner 
  -- osrt by multiple columns

--25 
SELECT pro_id, pro_name, pro_price, pro_com FROM item_mast
WHERE pro_price BETWEEN 200 AND 600

--26 
SELECT AVG(PRO_PRICE) FROM ITEM_mast
WHERE PRO_COM = 16

--27
SELECT PRO_NAME AS 'ITEM_NAME', PRO_PRICE AS 'Price in Rs'
FROM ITEM_mast

--28
SELECT PRO_PRICE, PRO_PRICE 
FROM ITEM_mast
WHERE PRO_PRICE >= 250
ORDER BY PRO_PRICE DESC, PRO_NAME

--29
SELECT PRO_COM, AVG(PRO_PRICE) FROM ITEM_mast
GROUP BY PRO_COM

--30 
SELECT PRO_NAME, PRO_PRICE FROM ITEM_mast
WHERE PRO_PRICE = (SELECT MIN(PRO_PRICE) FROM ITEM_mast)

--31 
SELECT DISTINCT EMP_LNAME FROM EMP_DETAILS

--32
SELECT * FROM emp_details 
WHERE EMP_LNAME = 'Snares'

--33
SELECT * FROM EMP_DETAILS
WHERE EMP_DEPT = 57

