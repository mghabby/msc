-- Final SQL Script for Millie's Musical Emporium
-- Author: Mina Ghabrial

-- SECTION 1: Drop Existing Tables and Procedures
-- I'm doiing this to avoid conflicts.
DO $$
BEGIN
    -- Drop procedures if they exist
    DROP PROCEDURE IF EXISTS register_customer(varchar, text, varchar, date, varchar, text, varchar, varchar);
    DROP PROCEDURE IF EXISTS purchase_product(INT, INT, TIMESTAMP);
    DROP PROCEDURE IF EXISTS restock_product(INT, INT);
    DROP PROCEDURE IF EXISTS generate_sales_report(DATE, DATE);
    DROP PROCEDURE IF EXISTS transfer_stock(INT, INT, INT);
    DROP PROCEDURE IF EXISTS generate_store_sales_report(INT, DATE, DATE);
    
    -- Drop tables if they exist
    DROP TABLE IF EXISTS purchases CASCADE;
    DROP TABLE IF EXISTS products CASCADE;
    DROP TABLE IF EXISTS stores CASCADE;
    DROP TABLE IF EXISTS customers CASCADE;
END $$;

-- SECTION 2: Create Tables
-- Customers, products, stores, and purchases tables.
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    telephone VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    bank_name VARCHAR(100) NOT NULL,
    bank_address TEXT NOT NULL,
    sort_code VARCHAR(10) NOT NULL,
    account_number VARCHAR(20) NOT NULL
);

CREATE TABLE stores (
    store_id SERIAL PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    cost NUMERIC(10, 2) NOT NULL,
    stock_level INT NOT NULL CHECK (stock_level >= 0),
    store_id INT NOT NULL REFERENCES stores(store_id) ON DELETE CASCADE
);

CREATE TABLE purchases (
    purchase_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    purchase_date TIMESTAMP NOT NULL DEFAULT NOW(),
    delivery_date TIMESTAMP NOT NULL
);

-- SECTION 3: Insert Sample Data
-- Adding stores, products, and customers with Egyptian Artists & The Beatles.

-- Stores
INSERT INTO stores (store_name, location)
VALUES
('Liverpool Music Emporium', '251 Menlove Avenue, Liverpool'),
('Cairo Music House', '15 Al-Nahda Street, Cairo');

-- Customers
INSERT INTO customers (name, address, telephone, dob, bank_name, bank_address, sort_code, account_number)
VALUES
('John Doe', '123 Music Lane', '01234567890', '1985-06-15', 'Harmony Bank', '45 Bank Street', '123456', '987654321'),
('Jane Smith', '456 Rhythm Road', '09876543210', '1990-02-28', 'Melody Bank', '12 Bank Avenue', '654321', '123456789'),
('Umm Kulthum', '15 Al-Nahda Street, Cairo', '01111222333', '1904-12-31', 'National Bank of Egypt', '1 Tahrir Square, Cairo', '101010', '111122223333'),
('John Lennon', '251 Menlove Avenue, Liverpool', '01512345678', '1940-10-09', 'Barclays Bank', '10 Castle Street, Liverpool', '505050', '555566667777');

-- Products
INSERT INTO products (type, name, description, cost, stock_level, store_id)
VALUES
('Instrument', 'Guitar', 'Acoustic guitar', 299.99, 10, 1),
('Instrument', 'Piano', 'Electric piano', 499.99, 5, 1),
('Media', 'Sheet Music', 'Classical music sheet', 19.99, 50, 2),
('Instrument', 'Oud', 'Traditional Arabic string instrument', 150.00, 20, 2);

-- Purchases
INSERT INTO purchases (customer_id, product_id, purchase_date, delivery_date)
VALUES
(1, 1, NOW(), '2025-01-01 10:00:00'),
(2, 2, NOW(), '2025-01-05 15:00:00');

-- SECTION 4: Create Stored Procedures

-- 4.5 Transfer Stock
-- Stock transfers between stores for a specific produtc.
CREATE OR REPLACE PROCEDURE transfer_stock(
    p_product_id INT,
    p_source_store INT,
    p_target_store INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_stock_level INT;
BEGIN
    -- Check source store stock
    SELECT stock_level INTO v_stock_level FROM products WHERE product_id = p_product_id AND store_id = p_source_store;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Product % not found in source store %.', p_product_id, p_source_store;
    END IF;

    IF v_stock_level <= 0 THEN
        RAISE EXCEPTION 'Not enough stock to transfer.';
    END IF;

    -- Deduct stock from source store
    UPDATE products SET stock_level = stock_level - 1 WHERE product_id = p_product_id AND store_id = p_source_store;

    -- Add stock to target store
    INSERT INTO products (type, name, description, cost, stock_level, store_id)
    SELECT type, name, description, cost, 1, p_target_store
    FROM products
    WHERE product_id = p_product_id;

    RAISE NOTICE 'Product % successfully transferred from store % to store %.', p_product_id, p_source_store, p_target_store;
END;
$$;

-- 4.6 Generate Store Sales Report
-- this is for a specific store and date range.
CREATE OR REPLACE PROCEDURE generate_store_sales_report(
    p_store_id INT,
    p_start_date DATE,
    p_end_date DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN (
        SELECT c.name AS customer_name, p.name AS product_name, pu.purchase_date, pu.delivery_date
        FROM purchases pu
        JOIN customers c ON pu.customer_id = c.customer_id
        JOIN products p ON pu.product_id = p.product_id
        WHERE p.store_id = p_store_id AND pu.purchase_date BETWEEN p_start_date AND p_end_date
    )
    LOOP
        RAISE NOTICE 'Store % - Customer: %, Product: %, Purchase Date: %, Delivery Date: %',
            p_store_id, rec.customer_name, rec.product_name, rec.purchase_date, rec.delivery_date;
    END LOOP;
END;
$$;

-- SECTION 5: Test Cases
-- Testing the addedd features 

-- Testing transfer_stock
CALL transfer_stock(1, 1, 2); -- Valid transfer
-- CALL transfer_stock(1, 1, 999); -- Invalid target store

-- Testing generate_store_sales_report
CALL generate_store_sales_report(1, '2024-01-01', '2025-01-01'); -- Valid range
-- CALL generate_store_sales_report(1, '2025-01-01', '2024-01-01'); -- Invalid range
