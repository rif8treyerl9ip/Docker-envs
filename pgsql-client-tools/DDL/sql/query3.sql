CREATE TABLE customers (
   id SERIAL PRIMARY KEY,
   cust_name VARCHAR(100) NOT NULL,
   email VARCHAR(100) NOT NULL,
   phone VARCHAR(20),
   address TEXT
);

CREATE TABLE items (
   item_id SERIAL PRIMARY KEY,
   item_name VARCHAR(100) NOT NULL,
   item_desc TEXT,
   item_price DECIMAL(10,2) NOT NULL,
   item_stock INT NOT NULL
);

CREATE TABLE purchases (
   purchase_id SERIAL PRIMARY KEY,
   cust_id INT NOT NULL,
   purchase_date DATE NOT NULL,
   total_amount DECIMAL(10,2) NOT NULL,
   FOREIGN KEY (cust_id) REFERENCES customers(id)
);

CREATE TABLE purchase_details (
   detail_id SERIAL PRIMARY KEY,
   purchase_id INT NOT NULL,
   item_id INT NOT NULL,
   quantity INT NOT NULL,
   price DECIMAL(10,2) NOT NULL,
   FOREIGN KEY (purchase_id) REFERENCES purchases(purchase_id),
   FOREIGN KEY (item_id) REFERENCES items(item_id)
);
