from turtle import update
import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root"
)

cursor = db.cursor()

def show_dbs():
	query = "SHOW DATABASES"
	cursor.execute(query)

	for dbs in cursor:
		print(dbs)

def show_tables():
	query = "SHOW TABLES"
	cursor.execute(query)
	for tables in cursor:
		print(tables)

def create_db(db_name):
	query = "CREATE DATABASE {}".format(db_name)
	try:
		cursor.execute(query)
		print('\nDatabase {} created'.format(db_name))
	except:
		print("\nError in query execution")

def select_db(db_name):
	query = "USE {}".format(db_name)
	try:
		cursor.execute(query)
		print('\nDatabase {} in use'.format(db_name))
	except:
		print("\nInvalid Database name")

def show_table(table_name):
	query = "SELECT * FROM " + table_name
	try:
		cursor.execute(query)
		for row in cursor:
			print(row)
	except:
		print('\nInvalid Table name')

def create_table(table_details):
	query = table_details
	try:
		cursor.execute(query)
		print(cursor)
	except:
		print('\nInvalid Table query')

def drop_table(table_name):
	query = "DROP TABLE {}".format(table_name)
	try:
		cursor.execute(query)
	except:
		print('\nError droping table')

def drop_db(db_name):
	query = "DROP DATABBASE {}".format(db_name)
	try:
		cursor.execute(query)
	except:
		print('\nError while droping database')

def add_column(column_query):
	query = column_query
	try:
		cursor.execute(query)
	except:
		print('\nError while adding column')

def modify_column(column_query):
	query = column_query
	try:
		cursor.execute(query)
	except:
		print('\nError while modifing column')

def drop_column(table_name, column_name):
	query = "ALTER TABLE {} DROP COLUMN {}".format(table_name, column_name)
	try:
		cursor.execute(query)
	except:
		print('\nError while droping column')

def insert_row(name, age, phno):
	query = "INSERT INTO test_table (name, age, phno) VALUES (%s,%s,%s)"
	try:
		cursor.execute(query, (name, age, phno))
		db.commit()
	except:
		print('\nError while inserting row')


def update_column(update_query):
	query = update_query
	try:
		cursor.execute(query)
		db.commit()
	except:
		print('Error while updating')

def describe_table(table_name):
	query = "DESCRIBE {}".format(table_name)
	try:
		cursor.execute(query)
		for row in cursor:
			print(row)
	except:
		print('\nError while describing tale')


def delete_row(id):
	query = "DELETE FROM test_table WHERE id = {}".format(id)
	try:
		cursor.execute(query)
		db.commit()
	except:
		print('\nError deeting row(s)') 

# table = (
# 	"CREATE TABLE test_table ("
# 	"id int(3) NOT NULL AUTO_INCREMENT,"
# 	"name varchar(20) NOT NULL,"
# 	"age int(3) NOT NULL,"
# 	"phno int(10) NOT NULL,"
# 	"created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
# 	"PRIMARY KEY (id)"
# 	")"
# )

# add_column_query = (
# 	"ALTER TABLE test_table "
# 	"add email varchar(100) NOT NULL "
# 	"AFTER phno"
# )

# mod_column_query = (
# 	"ALTER TABLE test_table "
# 	"MODIFY name varchar(30) NOT NULL"
# )

# update_column_query = (
# 	"UPDATE test_table "
# 	"SET name='Ray', phno=0 "
# 	"WHERE id=3"
# )

select_db('testDB')
print()
show_table('test_table')
