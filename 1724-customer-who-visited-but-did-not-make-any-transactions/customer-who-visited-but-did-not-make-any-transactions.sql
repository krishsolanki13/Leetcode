# Write your MySQL query statement below
with visitwotransactions as(
    select customer_id
    from Visits v
    left join Transactions t
    on v.visit_id = t.visit_id
    where t.transaction_id is Null
)
select customer_id, count(*) as count_no_trans
from visitwotransactions
group by customer_id;