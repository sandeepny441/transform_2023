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
select  year, subject, winner, xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,  categoryf
from nobel_win
where (year < 1970 and subject = 'Physiology')
UNION 
select  year, subject, winner, country,  categoryf
from nobel_win
where (year >= 1971 and subject = 'Peace')


