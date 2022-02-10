# created test_sales database
query = (
  "CREATE DATABASE test_sales"
)

# created test_production database
query = (
  "CREATE DATABASE test_production"
)

# ------------------------------------------------------------------------------
# use test_production database 
query = (
  "Use test_production"
)

# created brands table in test_production
query = (
  "CREATE TABLE brands ("
  "brand_id int,"
  "brand_name varchar(160) NOT NULL,"
  "PRIMARY KEY(brand_id)"
  ")"
)

# created categories table in test_production
query = (
  "CREATE TABLE categories ("
  "category_id int,"
  "category_name varchar(30) NOT NULL,"
  "PRIMARY KEY(category_id)"
  ")"
)

# created products table in test_production
query = (
  "CREATE TABLE products ("
  "product_id int,"
  "product_name varchar(4000) NOT NULL,"
  "brand_id int," 
  "category_id int,"
  "model_year date," # needs to be solvede
  "list_price int,"
  "PRIMARY KEY(product_id),"
  "FOREIGN KEY(brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE"
  "FOREIGN KEY(category_id) REFERENCES categories(category_id) ON DELETE SET NULL"
  ")"
)

# ------------------------------------------------------------------------------
# use test_sales database 
query = (
  "Use test_sales"
)

# created customers table in test_sales
query = (
  "CREATE TABLE customers ("
  "customer_id int,"
  "first_name varchar(50) NOT NULL,"
  "last_name varchar(0),"
  "phone int(12),"
  "email varchar(62) NOT NULL,"
  "street varchar(95) NOT NULL,"
  "city varchar(35) NOT NULL,"
  "state varchar(12) NOT NULL,"
  "zip_code int(6) NOT NULL,"
  "PRIMARY KEY(customer_id)"
  ")"
)

# created stores table in test_sales
query = (
  "CREATE TABLE stores ("
  "store_id int,"
  "store_name varchar(50) NOT NULL,"
  "phone int(12),"
  "email varchar(62) NOT NULL,"
  "street varchar(95) NOT NULL,"
  "city varchar(35) NOT NULL,"
  "state varchar(12) NOT NULL,"
  "zip_code int(6) NOT NULL,"
  "PRIMARY KEY(store_id)"
  ")"
)

# created staffs table in test_sales
query = (
  "CREATE TABLE staffs ("
  "staff_id int,"
  "first_name varchar(50) NOT NULL,"
  "last_name varchar(0),"
  "email varchar(62) NOT NULL,"
  "phone int(12) NOT NULL,"
  "active bool NOT NULL,"
  "store_id int,"
  "PRIMARY KEY(staff_id)"
  "FOREIGN KEY(store_id) REFERENCES stores(store_id) ON DELETE CASCADE"
  ")"
)

# adding foreign key to staffs table
query = (
  "ALTER TABLE staffs "
  "ADD FOREIGN KEY(manager_id) "
  "REFERENCES staffs(staff_id) "
  "ON DELETE SET NULL"
)

# created orders table in test_sales
query = (
  "CREATE TABLE orders ("
  "order_id int,"
  "customer_id int,"
  "order_status varchar(20) NOT NULL,"
  "order_date date NOT NULL,"
  "required_date date,"
  "shipped_date date,"
  "store_id int,"
  "staff_id int,"
  "PRIMARY KEY(order_id)"
  "FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL"
  "FOREIGN KEY(store_id) REFERENCES stores(store_id) ON DELETE SET NULL"
  "FOREIGN KEY(staff_id) REFERENCES staffs(staff_id) ON DELETE SET NULL"
  ")"
)

# created order_items table in test_sales
query = (
  "CREATE TABLE order_items ("
  "order_id int,"
  "item_id int,"
  "product_id int,"
  "quantity int,"
  "list_price int,"
  "discount int,"
  "PRIMARY KEY(order_id,item_id),"
  "FOREIGN KEY(order_id) REFERENCES orderss(order_id) ON DELETE CASCADE,"
  "FOREIGN KEY(product_id) REFERENCES test_production.products(product_id) ON DELETE SET NULL"
  ")"
)

# ------------------------------------------------------------------------------
# use test_production database 
query = (
  "Use test_production"
)

# created stocks table in test_production
query = (
  "CREATE TABLE stocks ("
  "store_id int,"
  "product_id int," 
  "quantity int,"
  "PRIMARY KEY(store_id, product_id),"
  "FOREIGN KEY(store_id) REFERENCES test_sales.stores(store_id) ON DELETE CASCADE"
  "FOREIGN KEY(product_id) REFERENCES products(product_id) ON DELETE CASCADE"
  ")"
)