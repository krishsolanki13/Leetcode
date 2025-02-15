# Write your MySQL query statement below

select machine_id, round(sum(difference)/count(*),3) as processing_time
from (select a1.machine_id, a1.process_id,(a2.timestamp-a1.timestamp) as difference
from Activity a1
join Activity a2 on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id and a1.activity_type = 'start' and a2.activity_type = 'end') sub_table
group by machine_id;