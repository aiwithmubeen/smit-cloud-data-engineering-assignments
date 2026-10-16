-- Assignment 6 CTEs

-- 6.1 — Rewrite this derived table query as a CTE:
/*
SELECT AVG(order_count) AS avg_orders
FROM (
    SELECT store_id, COUNT(*) AS order_count
    FROM sales.orders
    GROUP BY store_id
) AS store_counts;
*/
with store_counts as (
select store_id, count(*) as order_count
from sales.orders
group by store_id
)
select avg(order_count) as avg_orders
from store_counts;


-- 6.2 — Write a CTE called cte_high_value_products that returns products with list_price > 2000. 
-- Then query the CTE to return only Mountain Bikes from that list, joining to production.categories.
with cte_high_value_products as (
select product_id, product_name, category_id, list_price
from production.products
where list_price > 2000
)
select p.product_name, p.list_price, c.category_name
from cte_high_value_products p
join production.categories c
on p.category_id = c.category_id
where c.category_name = 'Mountain Bikes';


-- 6.3 — Write two CTEs in one WITH clause: one that counts orders per customer, and one that sums revenue per customer. 
-- Join them in the outer query to return customer_id, order_count, and total_revenue side by side.
with order_counts as (
select customer_id, count(*) as order_count
from sales.orders
group by customer_id
),
customer_revenue as (
select o.customer_id,
sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_revenue
from sales.orders o
join sales.order_items oi
on o.order_id = oi.order_id
group by o.customer_id
)
select oc.customer_id, oc.order_count, cr.total_revenue
from order_counts oc
join customer_revenue cr
on oc.customer_id = cr.customer_id;


-- 6.4 — Using a recursive CTE, generate a list of numbers from 1 to 10. 
-- Each row should have the number and its square (n * n).
with numbers as (
select 1 as n, 1 * 1 as square

union all

select n + 1, (n + 1) * (n + 1)
from numbers
where n < 10
)
select n, square
from numbers
option (maxrecursion 5); -- if we dont write the by default is 100


-- 6.5 — Using the recursive CTE org chart from section 9.6.2 as a starting point, modify it to also show the manager's first_name alongside each employee. 
-- Add a level column (0 for the top manager, 1 for their direct reports, 2 for the next level down).
with org_chart as (
select
staff_id,
first_name,
manager_id,
cast(null as varchar(50)) as manager_name,
0 as level
from sales.staffs
where manager_id is null

union all

select
s.staff_id,
s.first_name,
s.manager_id,
o.first_name as manager_name,
o.level + 1
from sales.staffs s
join org_chart o
on s.manager_id = o.staff_id
)
select staff_id, first_name, manager_name, level
from org_chart
order by level, first_name
option (maxrecursion 100);


-- 6.6 — Think About It: A CTE is defined once but referenced twice in the same outer query. 
-- A colleague says "CTEs are faster than subqueries because the database computes the result once and reuses it." 
-- Is this claim accurate? What would you need to do if you genuinely needed the result computed only once and reused?
-- A CTE is not always faster than a subquery.
-- If the result needs to be calculated once and reused,
-- ANS = a temporary table can be used.
