import sqlite3
#create database
connection= sqlite3.connect('store_transaction.db')
cursor =connection.cursor()

#create stores table
command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

#create a purchases table
command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_amount FLOAT, FOREIGN KEY (store_id) REFERENCES stores (store_id))"""

cursor.execute(command2)

#add to stores
cursor.execute("INSERT INTO stores VALUES(21, 'Kenya,KE')")
cursor.execute("INSERT INTO stores VALUES(95, 'Uganda,UG')")
cursor.execute("INSERT INTO stores VALUES(64, 'Tanzania,TZ')")

#add to purchases
cursor.execute("INSERT INTO purchases VALUES(54,21,15)")
cursor.execute("INSERT INTO purchases VALUES(23,64,21)")

#get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)
