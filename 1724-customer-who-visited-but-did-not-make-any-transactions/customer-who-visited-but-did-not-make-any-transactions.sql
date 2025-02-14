# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans
from (select customer_id
      from Visits
      where visit_id not in (select visit_id
                            from Transactions)) cust_tab
group by customer_id;