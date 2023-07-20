CREATE TABLE orders_dd (
    order_id INT,
    customer_id INT,
    trip_id INT,
    status VARCHAR(255),
    order_timestamp TIMESTAMP
);
INSERT INTO orders_dd (order_id, customer_id, trip_id, status, order_timestamp) 
VALUES 
(727424, 8472, 100463, 'completed successfully', '2022-06-05 09:12:00'),
(242513, 2341, 100482, 'completed incorrectly', '2022-06-05 14:40:00'),
(141367, 1314, 100362, 'completed incorrectly', '2022-06-07 15:03:00'),
(582193, 5421, 100657, 'never received', '2022-07-07 15:22:00'),
(253613, 1314, 100213, 'completed successfully', '2022-06-12 13:43:00');
(123456, 8473, 100464, 'completed successfully', '2022-06-06 10:13:00'),
(234567, 2342, 100483, 'completed incorrectly', '2022-06-06 15:41:00'),
(345678, 1315, 100363, 'completed incorrectly', '2022-06-08 16:04:00'),
(456789, 5422, 100658, 'never received', '2022-07-08 16:23:00'),
(567890, 1315, 100214, 'completed successfully', '2022-06-13 14:44:00'),
(678901, 8474, 100465, 'completed successfully', '2022-06-07 11:14:00'),
(789012, 2343, 100484, 'completed incorrectly', '2022-06-07 16:42:00'),
(890123, 1316, 100364, 'completed incorrectly', '2022-06-09 17:05:00'),
(901234, 5423, 100659, 'never received', '2022-07-09 17:24:00'),
(112345, 1316, 100215, 'completed successfully', '2022-06-14 15:45:00');