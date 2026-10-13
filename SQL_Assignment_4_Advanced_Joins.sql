-- Section 4 — GROUP BY & Aggregates
-- Task 20:  Count how many products exist in each category. Show category name and product count.
select cat.category_name, count(prod.product_id) as 'Product count' from production.categories as cat
inner join production.products as prod
on cat.category_id = prod.category_id
group by cat.category_name
-- Task 21:  Find the average list price of products per brand.
select brd.brand_name, AVG(prd.list_price) as 'Average price of product' from production.brands as brd
join production.products as prd
on brd.brand_id=prd.brand_id
group by brd.brand_name
-- Task 22:  For each store, count the total number of orders.
select strs.store_name, COUNT(ord.order_id) 'Total number of orders' from sales.stores as strs
join sales.orders as ord
on strs.store_id = ord.store_id
group by strs.store_name
-- Task 23:  Find the total revenue per order. Revenue = quantity × list_price × (1 - discount).
select ord.order_id, sum(ord_itm.quantity * ord_itm.list_price * (1 - ord_itm.discount)) Revenue from sales.orders as ord
join sales.order_items as ord_itm
on ord.order_id = ord_itm.order_id
group by ord.order_id
-- Task 24:  Find each customer's total number of orders. Sort by order count descending.
select cus.customer_id, count(ord.order_id) as 'Order count' from sales.customers as cus
join sales.orders as ord
on cus.customer_id = ord.customer_id
group by cus.customer_id 
order by 'Order count' desc
-- Task 25:  Find the brand that has the highest average product price.
select brd.brand_id, count(prd.product_id) from production.brands as brd
join production.products as prd
on brd.brand_id = prd.brand_id
group by brd.brand_id
having AVG(prd.list_price)
-- Task 26:  List categories that have more than 50 products.
select cat.category_id from production.categories as cat
inner join production.products as prd
on cat.category_id = prd.category_id
group by cat.category_id
having count(prd.product_id) > 50
-- Hint: Use the HAVING clause to filter grouped results.
-- Task 27:  For each store, find the total revenue generated across all orders.
select stor.store_name, SUM(ord_itm.quantity * ord_itm.list_price * (1 - ord_itm.discount)) as Revenue from sales.stores as stor
join sales.orders as ord
on stor.store_id = ord.store_id
join sales.order_items as ord_itm
on ord_itm.order_id = ord.order_id
group by stor.store_name
-- Task 28:  Find how many orders each staff member handled, and show only those who ha	ndled more than 50 orders.
select stf.email, Count(ord.order_id) OrdersCount from sales.orders as ord
join sales.staffs as stf
on ord.staff_id = stf.staff_id
group by stf.email