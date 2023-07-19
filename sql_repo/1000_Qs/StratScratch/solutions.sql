select shipment_id, weight from 
select (shipment_id, weight, 
ROW_NUMBER() over(partition by shipment_date order by shipment_date) as rn ) t 
where rn = 1