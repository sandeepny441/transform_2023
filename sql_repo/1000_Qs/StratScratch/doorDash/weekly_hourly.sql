SELECT DAYNAME(customer_placed_order_datetime) as weekday, 
HOUR(customer_placed_order_datetime) as hour, 
round(AVG(order_total + tip_amount - discount_amount - refunded_amount), 2) as avg_earnings
FROM doordash_delivery
GROUP BY weekday, hour;