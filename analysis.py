import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="VudrkdwgwihsaE33#",
 database="sakila"
)

mycursor = db.cursor()

mycursor.execute("SELECT COUNT(*) FROM actor GROUP BY first_name")

ergebnis = mycursor.fetchall()

for row in ergebnis:
 print(row)

db.close()