select * from orders o
where purch_amt > (select max(purch_amt) from custoemrs c 
                  where o.customer_id = c.customer_id)
        