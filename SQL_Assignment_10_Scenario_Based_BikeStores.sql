-- Scenario-Based SQL Assignment - BikeStores

-- Task 1: Build the Sales Detail Dataset

select
    o.order_id,
    o.order_date,
    c.first_name + ' ' + c.last_name as customer_name,
    s.store_name,
    st.first_name + ' ' + st.last_name as staff_name,
    p.product_name,
    cat.category_name,
    b.brand_name,
    oi.quantity,
    oi.list_price,
    oi.discount,
    oi.quantity * oi.list_price * (1 - oi.discount) as net_line_revenue
from sales.orders o
join sales.customers c on c.customer_id = o.customer_id
join sales.stores s on s.store_id = o.store_id
join sales.staffs st on st.staff_id = o.staff_id
join sales.order_items oi on oi.order_id = o.order_id
join production.products p on p.product_id = oi.product_id
join production.categories cat on cat.category_id = p.category_id
join production.brands b on b.brand_id = p.brand_id
where o.order_status = 4
order by o.order_date desc;


-- Task 2: Store Performance Summary

select
    s.store_name,
    count(distinct o.order_id) as number_of_orders,
    sum(oi.quantity) as total_units_sold,
    sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_net_revenue,
    sum(oi.quantity * oi.list_price * (1 - oi.discount))
        / count(distinct o.order_id) as average_order_value
from sales.stores s
join sales.orders o on o.store_id = s.store_id
join sales.order_items oi on oi.order_id = o.order_id
where o.order_status = 4
group by s.store_name
order by total_net_revenue desc;


-- Task 3: High-Value Customers

with customer_sales as (
    select
        c.customer_id,
        c.first_name + ' ' + c.last_name as customer_name,
        count(distinct o.order_id) as completed_order_count,
        sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_spending
    from sales.customers c
    join sales.orders o on o.customer_id = c.customer_id
    join sales.order_items oi on oi.order_id = o.order_id
    where o.order_status = 4
    group by c.customer_id, c.first_name, c.last_name
)
select
    customer_id,
    customer_name,
    completed_order_count,
    total_spending
from customer_sales
where total_spending > (select avg(total_spending) from customer_sales)
order by total_spending desc;


-- Task 4: Inventory Risk Report

select
    p.product_name,
    s.store_name,
    st.quantity as current_quantity,
    cat.category_name,
    b.brand_name
from production.stocks st
join production.products p on p.product_id = st.product_id
join sales.stores s on s.store_id = st.store_id
join production.categories cat on cat.category_id = p.category_id
join production.brands b on b.brand_id = p.brand_id
where st.quantity < 5
order by
    case when st.quantity = 0 then 0 else 1 end,
    st.quantity,
    p.product_name;


-- Task 5: Top Products Within Each Category

with product_sales as (
    select
        p.product_id,
        p.category_id,
        cat.category_name,
        p.product_name,
        sum(oi.quantity) as total_units_sold,
        sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_net_revenue
    from production.products p
    join production.categories cat on cat.category_id = p.category_id
    join sales.order_items oi on oi.product_id = p.product_id
    join sales.orders o on o.order_id = oi.order_id
    where o.order_status = 4
    group by p.product_id, p.category_id, cat.category_name, p.product_name
),
ranked_products as (
    select
        category_id,
        category_name,
        product_name,
        total_units_sold,
        total_net_revenue,
        dense_rank() over (
            partition by category_id
            order by total_net_revenue desc
        ) as product_position
    from product_sales
)
select
    category_name,
    product_name,
    total_units_sold,
    total_net_revenue,
    product_position
from ranked_products
where product_position <= 3
order by category_name, product_position, product_name;


-- Task 6: Monthly Sales Trend

with monthly_sales as (
    select
        year(o.order_date) as order_year,
        month(o.order_date) as order_month,
        sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_net_revenue
    from sales.orders o
    join sales.order_items oi on oi.order_id = o.order_id
    where o.order_status = 4
    group by year(o.order_date), month(o.order_date)
),
monthly_with_previous as (
    select
        order_year,
        order_month,
        total_net_revenue,
        lag(total_net_revenue) over (
            order by order_year, order_month
        ) as previous_month_revenue
    from monthly_sales
)
select
    order_year as year,
    order_month as month,
    total_net_revenue,
    previous_month_revenue,
    total_net_revenue - previous_month_revenue as revenue_change
from monthly_with_previous
order by year, month;


-- Task 7: Reusable Reporting View

create or alter view sales.vw_customer_sales_summary
as
select
    c.customer_id,
    c.first_name + ' ' + c.last_name as customer_name,
    count(distinct o.order_id) as total_completed_orders,
    coalesce(sum(oi.quantity), 0) as total_units_purchased,
    coalesce(sum(oi.quantity * oi.list_price * (1 - oi.discount)), 0) as total_net_revenue,
    max(o.order_date) as most_recent_completed_order_date
from sales.customers c
left join sales.orders o
    on o.customer_id = c.customer_id
    and o.order_status = 4
left join sales.order_items oi on oi.order_id = o.order_id
group by c.customer_id, c.first_name, c.last_name;
go

select * from sales.vw_customer_sales_summary;


-- Task 8: Safe Data Modification

begin transaction;

update sales.customers
set phone = '(999) 555-0101'
where customer_id = 1;

-- Validation
select customer_id, first_name, last_name, phone
from sales.customers
where customer_id = 1;

-- Roll back during testing
rollback transaction;

-- Use commit transaction instead of rollback when the change should be saved.


-- Task 9: Store Sales Procedure

create or alter procedure sales.usp_store_sales_report
    @store_id int,
    @start_date date,
    @end_date date
as
begin
    set nocount on;

    if @start_date > @end_date
    begin
        throw 50001, 'Start date cannot be later than end date.', 1;
    end;

    select
        p.product_name,
        sum(oi.quantity) as total_units_sold,
        sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_net_revenue
    from sales.orders o
    join sales.order_items oi on oi.order_id = o.order_id
    join production.products p on p.product_id = oi.product_id
    where o.order_status = 4
        and o.store_id = @store_id
        and o.order_date >= @start_date
        and o.order_date < dateadd(day, 1, @end_date)
    group by p.product_name
    order by total_net_revenue desc;
end;
go

-- Example:
-- exec sales.usp_store_sales_report 1, '2018-01-01', '2018-12-31';


-- Task 10: Management Insight Query
-- Business question: Which products are generating the most revenue in each store?
-- It measures product revenue by store.
-- Management can use this to identify strong products in each store.

select
    s.store_name,
    p.product_name,
    sum(oi.quantity) as total_units_sold,
    sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_net_revenue
from sales.stores s
join sales.orders o on o.store_id = s.store_id
join sales.order_items oi on oi.order_id = o.order_id
join production.products p on p.product_id = oi.product_id
where o.order_status = 4
group by s.store_name, p.product_name
order by s.store_name, total_net_revenue desc;
