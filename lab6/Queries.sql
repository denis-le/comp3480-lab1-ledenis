USE my_guitar_shop;

-- 1. Show all products
SELECT *
FROM products;

-- 2. Show product name and category
SELECT product_name, category_name
FROM products
INNER JOIN categories
ON products.category_id = categories.category_id;

-- 3. Show customer name and shipping address
SELECT first_name, last_name, line1
FROM customers
INNER JOIN addresses
ON customers.shipping_address_id = addresses.address_id;

-- 4. Show customer name and billing address
SELECT first_name, last_name, line1
FROM customers
INNER JOIN addresses
ON customers.billing_address_id = addresses.address_id;

-- 5. Show customer name and product ordered
SELECT c.first_name, c.last_name, p.product_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id;

-- 6. Show product name and discount if discount is over 30
SELECT p.product_name, oi.discount_amount
FROM products p 
INNER JOIN order_items oi ON oi.product_id = p.product_id
WHERE p.discount_percent > 30;

-- 7. Show number of products in each category
SELECT p.category_id, COUNT(p.product_name) AS number_of_products
FROM products p
GROUP BY p.category_id;

-- 8. Show how many products had a certain discount
SELECT p.discount_percent, COUNT(p.product_id)
FROM products p
GROUP BY p.discount_percent
ORDER BY p.discount_percent DESC;

-- 9. Show customers per state
SELECT state, COUNT(c.customer_id) AS number_of_customers
FROM addresses a 
INNER JOIN customers c ON a.address_id = c.shipping_address_id
GROUP BY a.state
ORDER BY COUNT(c.customer_id) DESC;

-- 10. Show average price per category
SELECT c.category_name, AVG(p.list_price) AS average_price
FROM categories c 
INNER JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_name;

-- 11. Show number of orders per customer
SELECT c.first_name, c.last_name, COUNT(o.order_id) AS total_orders
FROM orders o
INNER JOIN customers c ON c.customer_id = o.customer_id 
GROUP BY c.customer_id;