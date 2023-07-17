select customerNumber, creditlimit, 
sum(creditLimit) over(order by customerNumber) as cum_sum_price
from customers 