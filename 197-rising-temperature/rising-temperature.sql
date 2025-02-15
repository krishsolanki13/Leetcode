# Write your MySQL query statement below
-- select id
-- from (select id,recordDate, temperature, lag(temperature) over (order by recordDate asc) as prev_temp
--       from Weather) prev_temp_table
-- where temperature > prev_temp;

select w1.id
from Weather w1 
join Weather w2 on datediff(w1.recordDate,w2.recordDate)=1
where w1.temperature>w2.temperature;