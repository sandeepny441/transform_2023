SELECT CURRENT_DATE


SELECT CURRENT_TIMESTAMP


SELECT EXTRACT(YEAR FROM order_date) 
FROM orders


SELECT DATE_ADD(order_date, INTERVAL 30 DAY) 
FROM orders


SELECT DATE_SUB(order_date, INTERVAL 1 MONTH)
FROM orders


SELECT DATEDIFF(order_date, shipped_date) 
FROM orders


SELECT DATE_FORMAT(order_date,'%m-%d-%Y') 
FROM orders 

SELECT ADD_MONTHS(order_date, 3)
FROM orders

SELECT LAST_DAY(order_date) 
FROM orders


