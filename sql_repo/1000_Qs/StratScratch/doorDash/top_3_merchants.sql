-- doorDash - 1
with ranking as 
(
select date(a.order_timestamp) as order_date,
       b.name,
       count(a.id) as order_count,
       dense_rank() over(partition by date(a.order_timestamp) 
       					order by count(a.id) desc) as rnk
from order_details a
inner join merchant_details b on a.merchant_id = b.id
group by 1,2
)

select order_date,
        name,
        rnk
from ranking
where rnk <= 3

--doorDash - 2 







 
 
