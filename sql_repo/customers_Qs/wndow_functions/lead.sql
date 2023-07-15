select customerName, creditLimit,
LAG(creditLimit) over(order by customerName desc) as prev_cust_credit_limit,
LEAD(creditLimit) over(order by customerName desc) as next_cust_credit_limit 
from customers