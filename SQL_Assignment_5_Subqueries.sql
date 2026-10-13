-- Section 5 — Subqueries
-- Task 29:  Find all products whose list price is above the overall average list price.
select * from production.products
where list_price > (select avg(list_price) from production.products)
-- Hint: Use a subquery in the WHERE clause with AVG().
-- Task 30:  Find customers who have never placed an order.
-- with not in operator
select * from sales.customers
where customer_id not in (select customer_id from sales.orders)
-- with not exist operator
select * from sales.customers as cus
where not exists (select 1 from sales.orders where customer_id = cus.customer_id)
-- Hint: Use NOT IN or NOT EXISTS with a subquery on sales.orders.
-- Task 31:  List the most expensive product in each category.
-- using subquery
select * from production.products as prd
where prd.product_id = (select top 1 p.product_id from production.products as p where prd.category_id = p.category_id order by list_price desc)
order by category_id asc;
-- using CTE
with MostExpensiveProducts as (
select 
	*,
	ROW_NUMBER() over(partition by category_id order by list_price desc) as RN
	from production.products
)
select * from MostExpensiveProducts
where RN = 1
-- Hint: Use a correlated subquery or a CTE with ROW_NUMBER().
-- Task 32:  Find staff members who work in the store that generated the most revenue.
select * from sales.staffs where store_id in (
	select top 1 strs.store_id from sales.stores as strs
	join sales.orders as ord
	on strs.store_id = ord.store_id
	join sales.order_items as ord_itm
	on ord.order_id = ord_itm.order_id
	group by strs.store_id
	order by max(ord_itm.quantity * ord_itm.list_price * (1 - ord_itm.discount)) desc
)
-- Task 33:  Find orders where the total order value exceeds 5000.
select * from sales.orders as ord
where ord.order_Id in (select ord_itm.order_id from sales.order_items as ord_itm 
	group by ord_itm.order_id
	having sum(ord_itm.quantity * ord_itm.list_price * (1 - ord_itm.discount)) > 5000
	)
-- Hint: Use a subquery to calculate order totals, then filter in the outer query.
-- Task 34:  List products that have never been ordered by any customer.
select * from production.products
where product_id not in (select product_id from sales.order_items)
-- Task 35:  Find the customer who has spent the most money overall.
select * from sales.customers 
where customer_id = (
select top 1 o.customer_id from sales.orders o
join sales.order_items oi
on o.order_id = oi.order_id
group by o.customer_id
order by SUM(oi.list_price * oi.quantity) desc
)
