-- Example DWH

DROP TABLE IF EXISTS dwh_pelanggan;
CREATE TABLE dwh_pelanggan (
	id_customer INT NOT NULL,
	name_customer VARCHAR(255),
	amount INT
	);

-- DROP TABLE IF EXISTS fact_order_items; 
-- CREATE TABLE fact_order_items (
-- 	order_item_id INT NOT NULL ,
-- 	order_id INT NOT NULL,
-- 	product_id INT NOT NULL,
-- 	order_item_quantity INT,
-- 	product_discount INT,
-- 	product_subdiscount INT,
-- 	product_price INT NOT NULL,
-- 	product_subprice INT NOT NULL
-- );