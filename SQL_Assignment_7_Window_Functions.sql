-- Assignment 7 Window Functions


-- 7.1
-- Write a query to assign a row number to every product,
-- and also assign a row number within each category based on list price.
select
row_number() over (order by list_price desc) as row_num,
row_number() over (
partition by category_id
order by list_price desc
) as category_row_num,
product_name,
category_id,
list_price
from production.products;


-- 7.2
-- Write a query to rank products by list price within each category.
-- Show both rank() and dense_rank().
select
product_name,
category_id,
list_price,
rank() over (
partition by category_id
order by list_price desc
) as price_rank,
dense_rank() over (
partition by category_id
order by list_price desc
) as dense_price_rank
from production.products;


-- 7.3
-- Write a query to compare each month's revenue with the previous
-- month's revenue for each store.
with monthly_sales as (
select
store_id,
year(order_date) as order_year,
month(order_date) as order_month,
sum(oi.quantity * oi.list_price * (1 - oi.discount)) as revenue
from sales.orders o
join sales.order_items oi
on o.order_id = oi.order_id
group by store_id, year(order_date), month(order_date)
)
select
store_id,
order_year,
order_month,
revenue as current_month_revenue,
lag(revenue) over (
partition by store_id
order by order_year, order_month
) as previous_month_revenue,
revenue - lag(revenue) over (
partition by store_id
order by order_year, order_month
) as revenue_change
from monthly_sales
order by store_id, order_year, order_month;


-- 7.4
-- Divide products into 5 groups based on their list price,
-- with the lowest prices in group 1 and highest prices in group 5.
select
product_name,
list_price,
ntile(5) over (order by list_price) as price_band
from production.products
order by list_price;


-- 7.5
-- Calculate a running total of revenue for all orders,
-- ordered by order date.
with order_revenue as (
select
o.order_id,
o.order_date,
sum(oi.quantity * oi.list_price * (1 - oi.discount)) as revenue
from sales.orders o
join sales.order_items oi
on o.order_id = oi.order_id
group by o.order_id, o.order_date
)
select
order_id,
order_date,
revenue,
sum(revenue) over (
order by order_date, order_id
rows between unbounded preceding and current row
) as running_total
from order_revenue
order by order_date, order_id;


-- 7.6
-- What is the difference between the default window frame
-- used by first_value() and last_value(), and why does
-- last_value() often need an explicit window frame?

-- Answer:
-- last_value() needs the full window frame to return the actual
-- last value of the partition. first_value() works with the
-- default frame because the first row is already included.
