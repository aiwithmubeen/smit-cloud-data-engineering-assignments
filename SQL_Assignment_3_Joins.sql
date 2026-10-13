-- Section 3 — JOINs
-- Task 12:  List every product along with its brand name and category name.
-- Hint: JOIN production.products with production.brands and production.categories.
select prod.*, brd.brand_name, cat.category_name from production.products as prod
inner join production.brands as brd
on prod.brand_id = brd.brand_id
inner join production.categories as cat
on prod.category_id = cat.category_id
-- Task 13:  List all orders with the customer's full name (first_name + last_name), order date, and order status.
select ord.order_date, ord.order_status, cus.first_name + ' ' + cus.last_name as 'Customer Name' from sales.orders as ord
inner join sales.customers as cus
on ord.customer_id = cus.customer_id
-- Task 14:  Show every order item with the product name, quantity, list price, and discount.
select prod.product_name, ord_item.quantity, prod.list_price, ord_item.discount from sales.order_items as ord_item
join production.products as prod
on ord_item.product_id = prod.product_id
-- Task 15:  List each staff member's full name alongside their store name.
select stf.first_name + ' ' + stf.last_name as 'Staff fullname', stre.store_name from sales.staffs as stf
join sales.stores as stre
on stf.store_id = stre.store_id
-- Task 16:  List staff members along with their manager's full name.
select * from sales.staffs 
select stf.first_name + ' ' + stf.last_name as 'Staff name',man.first_name + ' ' + man.last_name as 'Manager name'  
from sales.staffs as stf
left join sales.staffs as man
on stf.manager_id = man.staff_id
-- Hint: Use a self-join on the sales.staffs table using manager_id.
-- Task 17:  Show all stores and the products they have in stock, including the product name and quantity. Only show items where quantity > 0.
select strs.store_name, prod.product_name, stk.quantity from production.stocks as stk
inner join sales.stores as strs
on stk.store_id = strs.store_id
inner join production.products as prod
on stk.product_id = prod.product_id
where stk.quantity > 0
-- Task 18:  List all customers who placed at least one order. Show customer name and order date.
select cus.first_name + ' ' + cus.last_name as 'Customer Name', ord.order_date from sales.customers as cus
inner join sales.orders as ord
on cus.customer_id = ord.customer_id
-- Hint: An INNER JOIN naturally eliminates non-ordering customers.
-- Task 19:  List ALL customers and their orders (if any). Customers who never ordered should still appear with NULL order data.
select cus.first_name + ' ' + cus.last_name as 'Customer Name', ord.order_date from sales.customers as cus
left join sales.orders as ord
on cus.customer_id = ord.customer_id
-- Hint: Use a LEFT JOIN.