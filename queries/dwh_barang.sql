-- Example DWH

DROP TABLE IF EXISTS dwh_barang;
CREATE TABLE dwh_barang (
	produk VARCHAR(255),
	tipe VARCHAR(255),
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