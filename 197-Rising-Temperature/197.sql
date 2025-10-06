-- -- Write your PostgreSQL query statement below
-- SELECT today.id
-- FROM Weather yesterday
-- CROSS JOIN Weather today
-- WHERE today.recordDate - yesterday.recordDate = 1 AND today.temperature > yesterday.temperature;

-- Write your PostgreSQL query statement below
select w1.id 
from Weather as w1
join Weather as w2 
on w1.recordDate = w2.recordDate + interval '1 day'
where w1.temperature > w2.temperature 