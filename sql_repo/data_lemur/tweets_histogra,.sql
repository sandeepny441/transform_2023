 
SELECT tweet_count as tweet_bucket,
count(DISTINCT user_id) as users_num
from (select user_id, count(tweet_id) as tweet_count from tweets 
where extract(year from tweet_date) = 2022 
group by user_id) as temp_SQ 
group by tweet_bucket 
