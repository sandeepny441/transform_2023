select d.employee_id, 
CASE when SUM(d.deal_size) >= sq.quota then 'Yes'
ELSE 'No'
END as made_quota 
from deals d inner join sales_quotas sq 
on d.employee_id = sq.employee_id
GROUP BY d.employee_id
ORDER BY d.employee_id
